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

4. Get an API key from [OpenWeatherMap](https://openweathermap.org/api)

5. Update `weather.py` with your API key:
```python
API_KEY = 'your-api-key-here'
```

## Usage

Run the application:
```bash
python weather.py
```

Open your browser and navigate to:
```
http://localhost:5000
```

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

## API

### GET `/`
Home page with search form.

### GET `/forecast`
Fetch weather forecast.

**Parameters:**
- `city` (required): City name
- `period` (required): 'daily' or 'weekly'

**Response:** Rendered weather template with data

## Error Handling

The app handles:
- 400: Bad Request (missing parameters)
- 404: City not found
- 500: Internal server errors

## Technologies

- **Backend**: Flask
- **API**: OpenWeatherMap
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Deployment**: Compatible with Heroku, PythonAnywhere, etc.

## License

MIT License — feel free to use this project as you wish.

## Contributing

Found a bug or want to improve? Feel free to open an issue or submit a pull request!

---

**Author**: 3mr3x  
**Last Updated**: December 2025
