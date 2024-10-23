# Weather Forecast API

This is a simple Flask-based API that provides weather forecast data, including short forecasts and temperature characterizations, based on latitude and longitude inputs. The data is fetched from the National Weather Service API.

## Requirements

- Python 3 or higher
- Flask
- Requests library

### Install Dependencies

Before running the app, install the required dependencies:

```bash
pip install Flask requests


How to Run
Step 1: Run the Flask Application
On Windows, open the command line and navigate to the directory containing the app.py file. Then, run the following command:

bash:
python app.py

Step 2: Open the URL
Once the Flask server is running, open your browser and go to the following URL:

http://127.0.0.1:5000
This will return a welcome message from the Weather Forecast channel.

Step 3: Get Short Forecast
To get the short forecast for a location, provide the latitude and longitude coordinates by appending them as query parameters to the following URL:

http://127.0.0.1:5000/shortForecast?lat=<latitude>&lon=<longitude>

Example: For New York City,
http://127.0.0.1:5000/shortForecast?lat=40.7128&lon=-74.0060
This will return the short weather forecast for New York City.

Step 4: Get Temperature Characterization
To get the temperature and its characterization (e.g., cold, moderate, hot) for a location, provide the latitude and longitude as query parameters to the following URL:

http://127.0.0.1:5000/temperature?lat=<latitude>&lon=<longitude>

Example: For New York City,
http://127.0.0.1:5000/temperature?lat=40.7128&lon=-74.0060

This will return the temperature characterization (cold, moderate, or hot) for New York City.

Endpoints
/
Method: GET
Description: Displays a welcome message.

/coordinates
Method: GET
Query Parameters:
	lat (required): Latitude of the location.
	lon (required): Longitude of the location.
Description: Returns the provided latitude and longitude in a JSON format.

/weatherForecast
Method: GET
Query Parameters:
	lat (required): Latitude of the location.
	lon (required): Longitude of the location.
Description: Fetches the weather forecast for a given latitude and longitude.

/shortForecast
Method: GET
Query Parameters:
	lat (required): Latitude of the location.
	lon (required): Longitude of the location.
Description: Returns a short description of the weather forecast for the provided coordinates.

/temperature
Method: GET
Query Parameters:
	lat (required): Latitude of the location.
	lon (required): Longitude of the location.
Description: Returns the temperature and its characterization (cold, moderate, or hot) for the provided coordinates.

Error Handling
If invalid latitude or longitude is provided, or the weather API fails to respond correctly, the API will return appropriate error messages in JSON format.