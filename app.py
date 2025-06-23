from flask import Flask, render_template, request
import requests

app = Flask(__name__)

import os
API_KEY = os.getenv("API_KEY")  # ← Yahan apni OpenWeatherMap wali API key daal

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    res = requests.get(url)
    if res.status_code == 200:
        return res.json()
    return None

@app.route("/", methods=["GET", "POST"])
def index():
    weather = None
    error = None
    if request.method == "POST":
        city = request.form.get("city")
        if city:
            weather = get_weather(city)
            if not weather:
                error = "City not found."
    return render_template("index.html", weather=weather, error=error)

if __name__ == "__bmain__":
    app.run(debug=True)