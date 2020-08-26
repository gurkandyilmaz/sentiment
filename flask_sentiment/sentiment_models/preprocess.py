import re


stopwords = []

def preprocess_data(text):
    """ 
    Remove stopwords, and words shorter than 2 characters.
    Remove Numbers, Punctuation and special chars.
    Make Lowercase. 
    """
    tokens = text.split()

    lowercase = _make_lowercase(tokens)
    cleaned = _remove_punc_nums_special_chars(lowercase)
    stopwords_removed = _remove_stopwords(cleaned)

    return " ".join(stopwords_removed)
  

def _make_lowercase(tokens):
    lowercased_tokens = []
    for token in tokens:
        lowercased_tokens.append(token.lower())

    return lowercased_tokens


def _remove_punc_nums_special_chars(tokens):
    cleaned_tokens = tokens.copy()
    for idx, token in enumerate(tokens):
        lower_i = "İ".lower()
        if lower_i in token:
            token = re.sub(f'{lower_i}', 'i', token)
        token = re.sub('[^a-zçşğöüİÖÜĞŞÇ]', ' ', token)
        cleaned_tokens[idx] = token.strip()

    return cleaned_tokens


def _remove_stopwords(tokens):
    if stopwords:
        stopwords_list = stopwords
    else:
        stopwords_list = _read_stopwords()
    tokens_copy = tokens.copy()
    for token in tokens:
        if (token in stopwords_list) or (len(token) < 3):
            tokens_copy.remove(token)
  
    return tokens_copy


def _read_stopwords(filename='stopwords'):
    with open(filename, 'r') as file:
        data = file.readlines()
        for word in data:
            stopwords.append(word.strip('\n'))
 
    return stopwords
