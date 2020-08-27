import os
import pickle
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

from flask import Flask, render_template

from sentiment_models import preprocess, vectorize, model
  
app = Flask(__name__)

max_features = 40000
max_sequence_length = 20
embedding_dim = 16


models_directory = os.path.join(os.getcwd(), 'sentiment_models')
tokenizer_file_path = os.path.join(models_directory, 'tokenizer.pickle')
lstm_model_path = os.path.join(models_directory, 'best_lstm.h5')

tokenizer = model.load_tokenizer(tokenizer_file_path)
lstm_model = model.load_model(lstm_model_path)

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/index')
def about():
    return 'about'

@app.route('/<input_string>')
def hello(input_string):
    result = model.predict_sentiment(input_string, tokenizer, lstm_model)
    return render_template('model/models.html', input_str=result)


if __name__ == '__main__':
    app.run()
