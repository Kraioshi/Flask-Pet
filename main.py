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
cat_url = os.getenv('CAT_URL')
dog_url = os.getenv('DOG_URL')
shiba_url = os.getenv('SHIBA_URL')

cat_headers = {
    'Authorization': f'Bearer {cat_api_key}',
}

dog_headers = {
    'Authorization': f'Bearer {dog_api_key}',
}


@app.route('/')
@app.route('/index')
def index():
    current_page = 'index'
    return render_template('index.html', current_page=current_page)


@app.route('/shiba')
def shiba():
    current_page = 'shiba'
    shiba_response = requests.get(url=shiba_url).json()[0]
    shiba_image = f'https://cdn.shibe.online/shibes/{shiba_response}.jpg'
    return render_template('shiba.html', current_page=current_page,
                           shiba_image=shiba_image)


@app.route('/cat')
def cat():
    current_page = 'cat'
    cat_response = requests.get(cat_url, headers=cat_headers).json()
    cat_image = cat_response[0]['url']
    return render_template('cat.html', current_page=current_page,
                           cat_image=cat_image)


@app.route('/dog')
def dog():
    current_page = 'dog'
    dog_response = requests.get(dog_url, headers=dog_headers).json()
    dog_image = dog_response[0]['url']
    return render_template('dog.html', current_page=current_page,
                           dog_image=dog_image)


if __name__ == '__main__':
    app.run(debug=True)
