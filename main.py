from flask import Flask, render_template
from dotenv import load_dotenv
import os
import requests

app = Flask(__name__)

load_dotenv()

cat_key = os.getenv('CAT')


@app.route('/')
def index():
    return render_template('cat.html')


if __name__ == '__main__':
    app.run(debug=True)
