import time

import tensorflow as tf
from tensorflow import keras


def transform_to_sequence_of_integers(text_list, tokenizer):
    sequence_of_integers = tokenizer.texts_to_sequences(text_list)

    return sequence_of_integers


def pad_sequences_of_integers(sequence_of_integers, max_sequence_length=20):
    padded_sequences = keras.preprocessing.sequence.pad_sequences(sequence_of_integers, padding='post', truncating='post', maxlen=max_sequence_length)
    
    return padded_sequences




