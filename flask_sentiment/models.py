import functools
import os

from flask import Blueprint, redirect, render_template, request, url_for

from flask_sentiment.sentiment_models import *
from tensorflow import keras

bp = Blueprint('models', __name__, url_prefix='/models')

model_path = os.path.join(os.getcwd(), 'flask_sentiment/sentiment_models/best_model_embed_lstm.h5')
#model = keras.models.load_model(model_path)

print(os.listdir('./flask_sentiment/sentiment_models'))
@bp.route('/<input_string>')
def make_prediction(input_string):
    #result = model.predict(['hadi'])
    return render_template('model/models.html', input_str=input_string, result=result)
