from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "Index Page"

@app.route('/index')
def about():
    return 'about'

@app.route('/<string:isim>/<int:yas>')
def hello(isim, yas):
    return "NAME: *{0}*. YAS: {1} type_name: {2} type_yas: {3}".format(isim, yas, type(isim).__name__, type(yas).__name__)
