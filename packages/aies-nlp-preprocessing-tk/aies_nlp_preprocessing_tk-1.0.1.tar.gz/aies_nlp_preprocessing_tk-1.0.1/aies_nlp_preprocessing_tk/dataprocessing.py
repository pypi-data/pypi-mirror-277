import pandas as pd

class InvalidCSVFormatError(Exception):
    """Custom exception to indicate invalid CSV format."""
    pass


def determine_label_type(data_frame: pd.DataFrame) -> str:
    """
    Determines the label type of a DataFrame based on the presence of '|' characters in the 'tag' column.

    Parameters:
    data_frame (pd.DataFrame): DataFrame containing the dataset.

    Returns:
    str: Type of label. Can be 'single' for single label or 'multi' for multi label.

    Example usage:
    data_frame = pd.read_csv("tweets.csv")
    label_type = determine_label_type(data_frame)

    """
    if len(data_frame.columns) != 2:
        data_frame = pd.DataFrame(columns=['tag', 'text'])
    else:
        if list(data_frame.columns) != ['tag', 'text']:
            data_frame.columns = ['tag', 'text']

    if not data_frame.empty and list(data_frame.iloc[0]) == ['tag', 'text']:
        data_frame = data_frame.iloc[1:]

    if any(data_frame['tag'].str.contains(r'\|')):
        return 'multi'
    else:
        return 'single'


def validate_csv_format(data_frame: pd.DataFrame, label_type: str) -> bool:
    """
    Validates the format of a DataFrame of tweets according to the specified label type.

    Parameters:
    data_frame (pd.DataFrame): DataFrame containing tweets loaded from a CSV.
    label_type (str): Type of validation to be performed. Can be 'single' for single label
                      or 'multi' for multi label.

    Returns:
    bool: True if the format is correct.

    Raises:
    InvalidCSVFormatError: If the CSV format is invalid.
    ValueError: If the 'label_type' parameter is invalid.

    Example usage:
    data = pd.read_csv("data.csv")
    try:
        validate_csv_format(data, 'single')
        print("CSV validated successfully.")
    except InvalidCSVFormatError as e:
        print(f"CSV validation error: {e}")

    """
    if label_type not in ['single', 'multi']:
        raise ValueError("The 'label_type' parameter must be 'single' or 'multi'.")

    if data_frame.shape[1] != 2:
        raise InvalidCSVFormatError("The CSV must contain exactly 2 columns.")
    
    data_frame.columns = ['tag', 'text']

    if label_type == 'single':
        if any(data_frame['tag'].str.contains(r'\|')):
            raise InvalidCSVFormatError("For single label, the 'tag' column must contain only one class per row.")

    elif label_type == 'multi':
        invalid_tags = data_frame['tag'].apply(lambda x: any(part == '' for part in x.split('|')))
        if invalid_tags.any():
            raise InvalidCSVFormatError("For multi label, the 'tag' column must contain classes separated by '|' without trailing or leading '|'.")

        if any(data_frame['tag'].str.match(r'^[A-Za-z]+(\|[A-Za-z]+)*$') == False):
            raise InvalidCSVFormatError("For multi label, the 'tag' column must contain valid classes separated by '|'.")

    return True


def dataframe_summary(data_frame: pd.DataFrame) -> dict:
    """
    Generates a summary dictionary with key statistics from the given DataFrame.

    Parameters:
    data_frame (pd.DataFrame): DataFrame containing the dataset.

    Returns:
    dict: Dictionary containing the main statistics of the DataFrame.

    Example usage:

    data = pd.read_csv("data.csv")
    summary = dataframe_summary(data)
    """
    total_records = len(data_frame)
    null_records = data_frame.isnull().sum().sum()
    unique_tags = data_frame['tag'].unique().tolist()
    records_per_tag = data_frame['tag'].value_counts().to_dict()
    text_lengths = data_frame['text'].str.len()
    text_length_distribution = {
        'min_length': text_lengths.min(),
        'max_length': text_lengths.max(),
        'mean_length': text_lengths.mean(),
        'median_length': text_lengths.median()
    }
    summary = {
        'total_records': total_records,
        'null_records': null_records,
        'unique_tags': unique_tags,
        'records_per_tag': records_per_tag,
        'text_length_distribution': text_length_distribution
    }
    return summary
