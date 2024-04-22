from flask import Flask, render_template
import requests
app = Flask(__name__)
def fetch_restaurant_data():
    url = "https://uk.api.just-eat.io/discovery/uk/restaurants/enriched/bypostcode/EC4M7RF"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    } #ensure compatibility to fetch data on most browsers and prevent auhentication error 403
    response = requests.get(url, headers=headers)
    if response.status_code == 200: #data fetch validation
        data = response.json()
        return data.get('restaurants', [])
    else:
        return []
@app.route('/')
def index():
    restaurants = fetch_restaurant_data()
    return render_template('index.html', restaurants=restaurants)
if __name__ == '__main__':
    app.run()

