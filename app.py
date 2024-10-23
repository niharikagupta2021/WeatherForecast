from flask import Flask,request,jsonify
import requests

app = Flask(__name__)

#Home route that returns a welcome message. 
@app.route('/', methods=['GET'])
def home():
    return "Hello, Welcome to Weather Forecast channel"

"""
    fetch weather forecast data for a given latitude and longitude
    query parameters:
    lat(str) : latitude of the location
    lon(str) : longitude of the location

    returns:
    JSON: A json response containing weather forecast data
    HTTP 500: If there is an error with the response structure or while parsing the forecast

"""
@app.route('/weatherForecast', methods=['GET'])
def getWeather():

    #get latitude and longitude 
    latitude = request.args.get('lat')
    longitude = request.args.get('lon')

    #get the response url
    url = f"https://api.weather.gov/points/{latitude},{longitude}"
    response = requests.get(url)


    if response.status_code != 200:
        return jsonify({"error": "Error fetching forecast data", "status_code": response.status_code, "response": response.text}), response.status_code

    
    #use try and except block to catch errors
    try:
        foreCastUrl = response.json()["properties"]["forecast"]
    except KeyError:
        return jsonify({"error": "Unexpected response structure from weather API"}), 500
    
    
    #get the response from the forecast API endpoint    
    forecast = requests.get(foreCastUrl)

    if forecast.status_code != 200:
            return jsonify({"error": "Error fetching forecast data", "status_code": response.status_code, "response": response.text}), response.status_code
    
    #use try and except block to cath errors
    try:
        forecastData = forecast.json()
        return forecastData
    except ValueError:
        return jsonify({"error": "Error parsing forecast Data"}),500
    
"""
    Fetch and return a short forecast description for the current weather.

    Returns:
        JSON: A JSON response containing a short forecast description.
        HTTP 500: If the response structure is unexpected.
"""
@app.route('/shortForecast',methods = ["GET"])
def shortForecast():
    #get response of the forecast API endpoint
    forecastData = getWeather()
    if isinstance(forecastData,tuple):
        return forecastData
    
    
    try:
        #extract the short forecast from forecast data
        shortForecast = forecastData["properties"]["periods"][0]["shortForecast"]
        return jsonify({"shortForecast": shortForecast})
    
    except KeyError:
        #handle error if the response structure is unexpected
        return jsonify({"Error":"Unexpected Response Structure from Forecast Data"}),500
    
    
@app.route('/temperature',methods = ["GET"])
def temparature():

    #get response from forecastData endpoint
    forecastData = getWeather()
    if isinstance(forecastData,tuple):
        return forecastData
    
    #use try and except block to catch errors
    try:
        # Extract the temperature from the forecast data
        temperature = forecastData["properties"]["periods"][0]["temperature"]
        if 45 <= temperature <= 73:
            output = jsonify({"temperature" : temperature,"description" :"moderate"})
        elif temperature < 45:
            output = jsonify({"temperature" : temperature,"description" :"cold"})
        elif temperature > 73:
            output = jsonify({"temperature" : temperature,"description" :"hot"})
    except:
        # Handle error if the response structure is unexpected
        return jsonify({"Error":"Unexpected Response Structure from Forecast Data"}),500

    return output


if __name__ == '__main__':
    app.run(debug = False)
