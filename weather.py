from flask import Flask, render_template, request, abort

import requests

app = Flask(__name__)

API_KEY = 'XXXXXXXXX'   

class WeatherAPI:
    def __init__(self, api_key):
        self.api_key = api_key

    def fetch_weather_data(self, city, period):
        if period == 'daily':
            base_url = 'http://api.openweathermap.org/data/2.5/weather'
        elif period == 'weekly':
            base_url = 'http://api.openweathermap.org/data/2.5/forecast'
        else:
            abort(400, 'Invalid period specified')

        complete_url = f"{base_url}?appid={self.api_key}&q={city}&units=metric"
        response = requests.get(complete_url)

        if response.status_code == 404:
            abort(404, f"City '{city}' not found.")
        elif response.status_code != 200:
            abort(500, f"API request failed with status code {response.status_code}: {response.text}")

        return response.json()

weather_api = WeatherAPI(API_KEY)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/forecast', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    period = request.args.get('period')

    if city is None or period is None:
        abort(400, 'Missing argument city or period')

    try:
        weather_data = weather_api.fetch_weather_data(city, period)

        if period == 'daily' and 'main' not in weather_data:
            abort(404, f"City '{city}' not found or invalid data returned by API.")
        elif period == 'weekly' and 'list' not in weather_data:
            abort(404, f"City '{city}' not found or invalid data returned by API.")

        return render_template('index.html', title='Weather Forecast', data=weather_data, period=period)
    except Exception as e:
        abort(500, f'Error fetching weather data: {e}')

# Error handlers
@app.errorhandler(400)
def bad_request_error(error):
    return render_template('simple_error.html', title='Bad Request', error_message=error.description), 400

@app.errorhandler(404)
def not_found_error(error):
    return render_template('simple_error.html', title='Not Found', error_message=error.description), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('simple_error.html', title='Internal Server Error', error_message=error.description), 500

if __name__ == "__main__":
    app.run(debug=True)
