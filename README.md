# Turkish Sentiment Analyzer

This repository contains a sentiment model built for Turkish language. The dataset consists of customer reviews on different services/products. <br /><br />

first clone this repository
```
$ git clone git@github.com:gurkandyilmaz/sentiment.git
```
cd into sentiment folder
```
$ cd sentiment/
```
create a virtual environment with either conda/pipenv/venv
```
$ conda create --name my_environment python=3.6
```
activate the environment
```
$ conda activate my_environment
```
install requirements
```
$(my_environment) pip install -r requirements.txt 
```
cd into sentiment/flask_sentiment/
```
$(my_environment) cd sentiment/flask_sentiment
```

run the flask app (app.py)
```
$(my_environment) flask run
```

