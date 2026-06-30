# My Weather App

A PyQt5-based desktop application that fetches and displays real-time weather information for any city using the OpenWeatherMap API.

## Features

- **City Search**: Enter any city name to get weather information
- **Real-time Weather Data**: Fetches current weather conditions using OpenWeatherMap API
- **Temperature Display**: Shows temperature in Celsius
- **Weather Emoji**: Displays weather condition as an emoji (thunderstorm, rain, snow, clouds, etc.)
- **Weather Description**: Shows a text description of the current weather
- **Error Handling**: Comprehensive error messages for various HTTP and connection errors
- **User-Friendly Interface**: Clean, centered GUI with large, readable fonts

## Weather Conditions Supported

The app recognizes and displays emojis for:
- ⛈️ Thunderstorm (ID: 200-232)
- 🌩️ Drizzle (ID: 300-321)
- 🌧️ Rain (ID: 500-531)
- ❄️ Snow (ID: 600-622)
- 🌫️ Mist/Fog (ID: 701-741)
- 🌋 Volcanic Ash (ID: 762)
- 💨 Squall (ID: 771)
- 🌪️ Tornado (ID: 781)
- ☀️ Clear Sky (ID: 800)
- ⛅ Cloudy (ID: 801-804)

## Prerequisites

Before running this application, ensure you have the following installed:

- Python 3.7+
- PyQt5
- requests

## Installation

1. Clone or download this repository:
```bash
git clone https://github.com/19-mohityadav/learning-python.git
cd learning-python/myWeather
```

2. Install required dependencies:
```bash
pip install PyQt5 requests
```

3. Get an API key from OpenWeatherMap:
   - Visit [OpenWeatherMap](https://openweathermap.org/api)
   - Sign up for a free account
   - Generate an API key from your account

## Configuration

1. Open `main.py` and replace the placeholder API key:
```python
api_key = "YOUR_API_KEY_HERE"
```

Replace `"API_KEY"` with your actual OpenWeatherMap API key.

## Usage

Run the application:
```bash
python main.py
```

1. A window titled "My Weather" will appear
2. Enter a city name in the input field (e.g., "London", "New York", "Tokyo")
3. Click the "Get Weather" button
4. The app will display:
   - Current temperature in Celsius
   - Weather condition emoji
   - Weather description

## Error Handling

The app handles the following errors gracefully:

- **Bad Request (400)**: Incorrect city name format
- **Unauthorized (401)**: Invalid API key
- **Forbidden (403)**: Access denied
- **Not Found (404)**: City not found
- **Internal Server Error (500)**: Server error, try again later
- **Bad Gateway (502)**: Invalid response from server
- **Service Unavailable (503)**: Server timeout
- **Connection Error**: Network connectivity issues
- **Timeout Error**: Request took too long
- **Too Many Redirects**: Redirect loop detected

## Project Structure

```
myWeather/
├── main.py          # Main application file
└── README.md        # This file
```

## Code Overview

### Main Components

- **MyApp Class**: Inherits from QWidget and manages the UI and weather data
- **init_ui()**: Initializes the user interface with labels, input field, and button
- **get_weather()**: Fetches weather data from OpenWeatherMap API
- **display_weather()**: Displays the weather information on the UI
- **display_error()**: Shows error messages when something goes wrong
- **get_weather_emoji()**: Returns appropriate emoji based on weather condition ID

## UI Layout

The application uses a vertical box layout (QVBoxLayout) containing:
- City label
- City input field
- Get Weather button
- Temperature display
- Weather emoji display
- Weather description

All elements are center-aligned with custom fonts and styling.

## API Reference

This app uses the OpenWeatherMap API:
- **Endpoint**: `https://api.openweathermap.org/data/2.5/weather`
- **Parameters**: 
  - `q`: City name
  - `appid`: Your API key

### Response Data Used

- `data["main"]["temp"]`: Temperature in Kelvin (converted to Celsius)
- `data["weather"][0]["id"]`: Weather condition ID
- `data["weather"][0]["description"]`: Weather description text

## Styling

The application uses custom QSS (Qt Style Sheet) styling:
- Large fonts for better readability
- Segoe UI Emoji font for weather emojis
- Center-aligned text
- Sans-serif font for labels and buttons

## Future Enhancements

Potential features to add:
- Forecast for multiple days
- Wind speed and humidity display
- Multiple city search history
- Temperature unit toggle (Celsius/Fahrenheit)
- Geographic location-based weather
- Save favorite cities
- Settings for API key management

## Troubleshooting

### "API_KEY error" or "Unauthorized"
- Make sure you've replaced the placeholder with a valid API key

### "City not found"
- Check the spelling of the city name
- Try using the full city name (e.g., "New York" instead of "NY")

### No response or timeout errors
- Check your internet connection
- Verify the OpenWeatherMap API is not experiencing downtime

### Import errors for PyQt5
- Reinstall PyQt5: `pip install --upgrade PyQt5`

## License

This project is part of a learning repository. Feel free to use, modify, and distribute as needed.

## Author

Created by: 19-mohityadav

## Resources

- [PyQt5 Documentation](https://www.riverbankcomputing.com/static/Docs/PyQt5/)
- [OpenWeatherMap API Documentation](https://openweathermap.org/api)
- [Requests Library Documentation](https://requests.readthedocs.io/)
