from flask import Flask, render_template, request
import requests

app = Flask(__name__)

api_key = 'b95127aa9e5141639e9150810242907'
base_url = 'http://api.weatherapi.com/v1/current.json'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        city = request.form['city']

        params = {'q': city, 'key': api_key}
        response = requests.get(base_url, params=params)

        if response.status_code == 200:
            weather_data = response.json()
            city_name = weather_data['location']['name']
            country = weather_data['location']['country']
            temperature = weather_data['current']['temp_c']
            weather_desc = weather_data['current']['condition']['text']

            return render_template('index.html', name=name, city=city_name, country=country, temperature=temperature, weather_desc=weather_desc)
        else:
            error_message = f"Error fetching data: {response.status_code} - {response.text}"
            return render_template('index.html', error=error_message)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
