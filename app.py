from flask import Flask,request

app = Flask(__name__)


weather_data = {
    'San Francisco': {'temperature': 14, 'weather': 'Cloudy'},
    'New York': {'temperature': 20, 'weather': 'Sunny'},
    'Los Angeles': {'temperature': 24, 'weather': 'Sunny'},
    'Seattle': {'temperature': 10, 'weather': 'Rainy'},
    'Austin': {'temperature': 32, 'weather': 'Hot'},
}

@app.route("/")
def greet():
    return "HELLO"



@app.route("/weather/",methods=["GET"])
def get_all():
    return weather_data

@app.route("/weather/<string:city>",methods=["GET"])
def weather(city):
    if city in weather_data:
        return weather_data[city]
    else:
        return "City not available"



@app.route("/weather/",methods=["POST"])
def add_city():
    data = request.get_json()
    city = data["city"]
    temperature = data["temperature"]
    weather = data["weather"]
    temp = {"temperature":temperature,"weather":weather}
    weather_data[city] = temp
    return weather_data
    

@app.route("/weather/<string:city>",methods=["PUT"])
def update_city(city):
    data = request.get_json()
    temperature = data["temperature"]
    weather = data["weather"]

    if temperature and weather:
        weather_data[city]["temperature"] = temperature
        weather_data[city]["weather"] = weather
    elif temperature:
        weather_data[city]["temperature"] = temperature
    elif weather:
        weather_data[city]["weather"] = weather
    else:
        return "PLease privide data",400
    
    return "Data updated"
    

@app.route("/weather/<string:city>",methods=["DELETE"])
def delete_city(city):
    if city in weather_data:
        del weather_data[city]
        return weather_data
    else:
        return "City not present",400
    
if __name__ =="__main__":
    app.run(debug=True)


