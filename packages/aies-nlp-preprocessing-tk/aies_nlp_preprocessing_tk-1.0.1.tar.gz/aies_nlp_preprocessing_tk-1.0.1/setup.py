from setuptools import setup, find_packages

setup(
    name='aies_nlp_preprocessing_tk',
    version='1.0.1',
    packages=find_packages(),
    install_requires=[
        
    ],
    author='João Victor Godoi Bernardino',
    author_email='joaogodoi1010@gmail.com',
    description='Set of NLP preprocessing techniques with the aim of abstracting data preparation processes, in addition to performing validations and cleaning the masses.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/JoaoGodoi/aies-nlp-preprocessing-tk',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)