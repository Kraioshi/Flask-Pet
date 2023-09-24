from flask import Flask, render_template
from dotenv import load_dotenv
import os
import requests

app = Flask(__name__)

load_dotenv()

api_key = os.getenv('CAT')
url = 'https://api.thecatapi.com/v1/images/search'

headers = {
    'Authorization': f'Bearer {api_key}',
}


@app.route('/')
def index():
    response = requests.get(url, headers=headers).json()
    cat_url = response[0]['url']
    return render_template('cat.html', cat_url=cat_url)


if __name__ == '__main__':
    app.run(debug=True)
