from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from dotenv import load_dotenv
import os
import requests

app = Flask(__name__)
Bootstrap5(app)
load_dotenv()

cat_api_key = os.getenv('CAT')
dog_api_key = os.getenv('DOG')
cat_url = 'https://api.thecatapi.com/v1/images/search'
dog_url = 'https://api.thedogapi.com/v1/images/search'
shiba_url = 'http://shibe.online/api/shibes?count=[1]&urls=[true]&httpsUrls=[true]'

headers = {
    'Authorization': f'Bearer {cat_api_key}',
}


shiba_response = requests.get(url=shiba_url).json()[0]
shiba_image = f'https://cdn.shibe.online/shibes/{shiba_response}.jpg'


@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/cat')
# def cat():
#     response = requests.get(url, headers=headers).json()
#     cat_url = response[0]['url']
#     return render_template('cat.html', cat_url=cat_url)
#
# @app.route('/shiba')
# def shiba():
#


if __name__ == '__main__':
    app.run(debug=True)
