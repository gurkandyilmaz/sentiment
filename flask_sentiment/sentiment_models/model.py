import os
import pickle
from time import time
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'


import tensorflow as tf
from tensorflow import keras

from .preprocess import preprocess_data
from .vectorize import transform_to_sequence_of_integers, pad_sequences_of_integers

max_features = 40000
max_sequence_length = 20
embedding_dim = 16


def load_tokenizer(file_path):
    with open(file_path, 'rb') as handler:
        tokenizer = pickle.load(handler)

    return tokenizer


def load_model(model_path):
    
    return keras.models.load_model(model_path)


def predict_sentiment(input_text, tokenizer, model):
    print("RAW TEXT: ", input_text)
    processed_text = preprocess_data(input_text)
    print("PROCESSED: ", processed_text)
    transformed_text = transform_to_sequence_of_integers([processed_text], tokenizer)
    print("TRANSFORMED: ", transformed_text)
    padded_text = pad_sequences_of_integers(transformed_text)
    print("PADDED: ", padded_text)

    prediction = model.predict(padded_text)
    # transform the result it is between 0.0 and 1.0 (sigmoid) or -1.0 and 1.0 (tanh)
    sigmoid = tf.math.sigmoid(prediction)
    tanh = tf.math.tanh(prediction)

    return tanh


if __name__ == '__main__':
    tokenizer_path = os.path.join(os.getcwd(), 'tokenizer.pickle')
    model_lstm_path = os.path.join(os.getcwd(), 'best_lstm.h5')
    model_pooling_path = os.path.join(os.getcwd(), 'best_pooling.h5')

    # tokenizer takes list of texts.
    tokenizer = load_tokenizer(tokenizer_path)
    model_lstm = load_model(model_lstm_path)
    model_pooling = load_model(model_pooling_path)

    test_text = "Satacağınız"
    result = predict_sentiment(test_text, tokenizer, model_lstm)
    print(result.numpy())



