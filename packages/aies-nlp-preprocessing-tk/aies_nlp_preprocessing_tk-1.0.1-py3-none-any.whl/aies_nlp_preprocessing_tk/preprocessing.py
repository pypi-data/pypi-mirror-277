import pandas as pd
import spacy
import string

from nltk.stem.snowball import SnowballStemmer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, MultiLabelBinarizer
from keras_preprocessing.text import Tokenizer
from keras_preprocessing.sequence import pad_sequences
from keras.utils import to_categorical

from aies_nlp_preprocessing_tk.dataprocessing import validate_csv_format, determine_label_type, InvalidCSVFormatError

class PreProcessingError(Exception):
    """Custom exception to error in preprocessing."""
    pass


def raw_tokenization(data_frame: pd.DataFrame,
                     max_length: int, 
                     split_test_size: float = None, 
                     remove_stop_words: bool = False, 
                     remove_punctuation: bool = False, 
                     language: str = "portuguese"):
    """
    Tokenizes text data and prepares it for training a neural network model.

    Parameters:
    data_frame (pd.DataFrame): The input DataFrame containing 'text' and 'tag' columns.
    max_length (int): Maximum length of sequences after padding.
    split_test_size (float, optional): Size of the test dataset if splitting is needed. Defaults to None.
    remove_stop_words (bool, optional): Whether to remove stop words. Defaults to False.
    remove_punctuation (bool, optional): Whether to remove punctuation. Defaults to False.
    language (str, optional): Language to be used for tokenization. Defaults to "portuguese".

    Returns:
    tuple: If split_test_size is provided, returns tuple of train and test data and word index.
           Otherwise, returns tuple of data and word index.
    """
    label_type = determine_label_type(data_frame)
    try:
        validate_csv_format(data_frame, label_type=label_type)
    except InvalidCSVFormatError as e:
        raise PreProcessingError(e)

    #TODO ajustar aqui, colocar mais opções de linguagens e também deixar melhor apresentado o código
    if language == "portuguese":
        nlp = spacy.load("pt_core_news_sm")
    else:
        raise ValueError(f"Language '{language}' is not supported.")

    def _process_text(text):
        doc = nlp(text)
        tokens = []
        for token in doc:
            if remove_punctuation and token.text in string.punctuation:
                continue
            if remove_stop_words and token.is_stop:
                continue
            if token.text.strip(): 
                tokens.append(token.text)
        return tokens

    data_frame['tokens'] = data_frame['text'].apply(_process_text)
    data_frame = data_frame[data_frame['tokens'].apply(len) > 0].reset_index(drop=True)
 
    tokenizer = Tokenizer(num_words=max_length)
    tokenizer.fit_on_texts(data_frame['tokens'])
    X = tokenizer.texts_to_sequences(data_frame['tokens'])
    X = pad_sequences(X, padding="post", maxlen=max_length)

    
    if label_type=='multi':
        data_frame['tag'] = data_frame['tag'].str.split('|')
        label_encoder = MultiLabelBinarizer()
    else:
        label_encoder = LabelEncoder()
        
    y = label_encoder.fit_transform(data_frame['tag'])
    y = to_categorical(y)

    if split_test_size is not None:
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=split_test_size)
        return X_train, X_test, y_train, y_test, tokenizer.word_index
    else:
        return X, y, tokenizer.word_index
