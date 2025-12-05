# Weather App — Flask

A modern Flask-based weather application that fetches real-time weather data from OpenWeatherMap API.

## Features

- 🌡️ **Real-time Weather**: Fetch current weather for any city
- 📅 **Daily & Weekly Forecast**: View daily weather or 5-day forecast
- 🎨 **Modern UI**: Clean, responsive design
- ⚡ **Fast & Lightweight**: Built with Flask and vanilla JavaScript
- 🛡️ **Error Handling**: Graceful error messages

## Installation

### Prerequisites
- Python 3.8+
- pip

### Setup

1. Clone the repository:
```bash
git clone https://github.com/3mr3x/weather-app-flask.git
cd weather-app-flask
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## API Key Setup

To use the Weather App, you need an OpenWeatherMap API key:

### Getting Your API Key:

1. **Visit OpenWeatherMap**: Go to [https://openweathermap.org/api](https://openweathermap.org/api)

2. **Sign Up**: Create a free account at [https://openweathermap.org/api](https://openweathermap.org/api)
   - Click "Sign Up" and fill in your details
   - Confirm your email address

3. **Get Your API Key**:
   - After login, go to your Account page
   - Click on the "API keys" tab
   - Copy your **Default API key**

4. **Add API Key to weather.py**:
   - Open `weather.py` in your text editor
   - Find this line: `API_KEY = 'XXXXXXXXX'`
   - Replace `'XXXXXXXXX'` with your actual API key:
   ```python
   API_KEY = 'your_actual_api_key_here'
   ```

### Example:
```python
# Before:
API_KEY = 'XXXXXXXXX'

# After (with your real key):
API_KEY = '1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p'
```

> ⚠️ **Important**: Never commit your API key to public repositories! Add `weather.py` to `.gitignore` if you plan to share this project.

## Usage

Run the application:
```bash
python weather.py
```

Open your browser and navigate to:
```
http://localhost:5000
```

### Example Searches:
- Search for "London" and select "Daily Forecast"
- Search for "New York" and select "Weekly Forecast (5 Days)"
- Try any city in the world!

## Project Structure

```
weather-app-flask/
├── weather.py              # Main Flask application
├── requirements.txt        # Python dependencies
├── templates/
│   ├── home.html          # Home/search page
│   ├── index.html         # Weather results page
│   ├── weather.html       # Detailed weather view
│   └── simple_error.html  # Error page
└── static/
    └── style.css          # CSS styles
```

## API Endpoints

### GET `/`
Home page with search form.

### GET `/forecast?city=<city>&period=<period>`
Fetch weather forecast.

**Parameters:**
- `city` (required): City name (e.g., "London", "Istanbul", "Tokyo")
- `period` (required): 'daily' or 'weekly'

**Example URLs:**
- `http://localhost:5000/forecast?city=London&period=daily`
- `http://localhost:5000/forecast?city=Istanbul&period=weekly`

**Response:** Rendered weather template with data

## Error Handling

The app handles:
- **400**: Bad Request (missing parameters)
- **404**: City not found
- **500**: Internal server errors

All errors display a friendly error page with information about what went wrong.

## Technologies

- **Backend**: Flask 3.0.0
- **API**: OpenWeatherMap
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **HTTP Client**: requests
- **Deployment**: Compatible with Heroku, PythonAnywhere, etc.

## Troubleshooting

### Issue: "City not found" error
- Make sure you have a valid API key in `weather.py`
- Check that the city name is spelled correctly
- Try using the English name of the city

### Issue: "Invalid API key" or API errors
- Verify your API key in `weather.py` is correct
- Check that your OpenWeatherMap account is active
- Make sure the Free tier plan is active in your OpenWeatherMap account

### Issue: Application won't start
- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Check Python version (3.8+ required)
- Verify port 5000 is not in use by another application

## License

MIT License — feel free to use this project as you wish.

## Contributing

Found a bug or want to improve? Feel free to open an issue or submit a pull request!

---

**Author**: 3mr3x  
**Last Updated**: December 2025
