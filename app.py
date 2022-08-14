from flask import Flask
import os
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

def create_app():
    app = Flask(__name__)
    app.config.from_object(os.environ['CONFIGURATION_SETUP'])

    @app.route('/')
    def index():
        return 'Success'

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000)