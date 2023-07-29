from flask import Flask, render_template
# Get public API key from https://newsapi.org/account
from config import API_KEY
import requests

app = Flask(__name__)

def get_latest_news(api_key, country_code, category=None):
    base_url = 'https://newsapi.org/v2/top-headlines'
    params = {
        'apiKey': api_key,
        'country': country_code,
    }

    if category:
        params['category'] = category

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        if data['status'] == 'ok':
            return data['articles']
        else:
            print('Error: Unable to fetch news data.')
    else:
        print('Error: Unable to connect to the API.')


@app.route('/')
def index():

    news_articles = get_latest_news(API_KEY, country_code='us')

    if news_articles:
        return render_template('index.html', articles=news_articles)
    else:
        return 'No news articles found.'

if __name__ == "__main__":
    app.run(debug=True)

