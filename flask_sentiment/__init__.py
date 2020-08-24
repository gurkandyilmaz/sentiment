import os

from flask import Flask, redirect, render_template, url_for


from flask_sentiment import sentiment_models

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
            SECRET_KEY='dev',
            DATABASE=os.path.join(app.instance_path, 'flask_sentiment.sqlite'),
     )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    from . import models
    app.register_blueprint(models.bp)

    print(os.listdir('./flask_sentiment/sentiment_models'))
    @app.route('/hello/')
    def hello():
        return 'MERHABE TELEVOEL'

    return app

