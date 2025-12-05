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

        data = response.json()
        return self._format_weather_data(data, period, city)

    def _format_weather_data(self, data, period, city):
        """Format API response data for template rendering"""
        formatted = {}
        
        if period == 'daily':
            # Format current weather data
            if 'main' in data and 'weather' in data:
                formatted['current_weather'] = {
                    'temp': data['main']['temp'],
                    'feels_like': data['main'].get('feels_like', data['main']['temp']),
                    'humidity': data['main']['humidity'],
                    'pressure': data['main']['pressure'],
                    'visibility': data.get('visibility', 10000),
                    'wind_speed': data['wind']['speed'],
                    'main': data['weather'][0]['main'],
                    'description': data['weather'][0]['description']
                }
                formatted['city'] = data.get('name', city)
                formatted['period'] = 'daily'
        
        elif period == 'weekly':
            # Format 5-day forecast data
            if 'list' in data:
                forecast_list = []
                seen_days = set()
                
                for item in data['list']:
                    dt_txt = item['dt_txt']
                    day = dt_txt.split(' ')[0]
                    
                    # Only include one forecast per day
                    if day not in seen_days:
                        seen_days.add(day)
                        forecast_list.append({
                            'date': day,
                            'temp': item['main']['temp'],
                            'condition': item['weather'][0]['main']
                        })
                
                formatted['forecast_data'] = forecast_list[:5]
                formatted['city'] = data.get('city', {}).get('name', city)
                formatted['period'] = 'weekly'
        
        return formatted

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
        formatted_data = weather_api.fetch_weather_data(city, period)
        
        # Check if data was formatted correctly
        if period == 'daily' and 'current_weather' not in formatted_data:
            abort(404, f"City '{city}' not found or invalid data returned by API.")
        elif period == 'weekly' and 'forecast_data' not in formatted_data:
            abort(404, f"City '{city}' not found or invalid data returned by API.")

        return render_template('index.html', 
                             title='Weather Forecast', 
                             **formatted_data)
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
