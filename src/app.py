import os

from flask import Flask, request
import src.functions as f

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/')
    def hello():
        return 'Hello, World!'
    
    @app.route('/count-words')
    def count_words_in_sentence():
        sentence = request.args.get("sentence")
        if sentence is None:
            return "0"
        broj = len(sentence.split())
        return str(broj)

    @app.route('/factorize')
    def test_factorize_number():
        number = request.args.get("number")
        message = request.args.get("message")
        n = int(number)
        if number is None:
            return message
        return f.factorize(n)
    
    @app.route('/number-of-digits')
        
    return app