from flask import Flask, request
import os
from dotenv import load_dotenv

app = Flask(__name__)


@app.route('/')
def home():
    return os.environ.get('HELLO', 'NO')


if __name__ == '__main__':
    load_dotenv()
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
