from flask import Flask
from weather import weather_by_city


app = Flask(__name__)

@app.route("/")
def hello():
    return weather_by_city

if __name__=="__main__":
    app.run()