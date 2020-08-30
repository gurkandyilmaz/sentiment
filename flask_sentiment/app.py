import os
import pickle
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
SECRET_KEY = os.urandom(32)

from flask import Flask, request, render_template, redirect, url_for, jsonify

from sentiment_models import preprocess, vectorize, model

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY


max_features = 40000
max_sequence_length = 20
embedding_dim = 16


models_directory = os.path.join(os.getcwd(), 'sentiment_models')
tokenizer_file_path = os.path.join(models_directory, 'tokenizer.pickle')
lstm_model_path = os.path.join(models_directory, 'best_lstm.h5')

tokenizer = model.load_tokenizer(tokenizer_file_path)
lstm_model = model.load_model(lstm_model_path)

@app.route('/', methods=['GET', 'POST'])
def index():
    result_dict = {}
    if request.method == "POST":
        form = request.form
        user_query = form.get('user_query', 'ERROR: user_text not found')
        sentiment_score = model.predict_sentiment(user_query, tokenizer, lstm_model)
        print("User TEXT: ", user_query)
        print("Sentimen SCORE: ", sentiment_score)
        
        result_dict['user_query'] = user_query
        result_dict['sentiment_score'] = sentiment_score

        return render_template('base.html', result=result_dict)
    
    result_dict['user_query'] = 'BOS'
    result_dict['sentiment_score'] = 'NaN'
    return render_template('base.html', result=result_dict)

@app.route('/predict/', methods=['POST'])
def predict():
    result_dict = {}
    user_request = request.json
    user_text = user_request.get('text', 'ERR: text not found.')
    sentiment_score = model.predict_sentiment(user_text, tokenizer, lstm_model)
    result_dict['text'] = user_text
    result_dict['sentiment_score'] = str(sentiment_score.numpy()[0][0])
    
    return jsonify(result_dict)

@app.route('/<input_string>')
def hello(input_string):
    
    return "hişşşssss"

if __name__ == '__main__':
    app.run(debug=True)
