from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/weather', methods=['POST'])
def weather():
    city = request.form['city']
    api_id = "117ecd9f300ed0c40d2aa31a32950e93"
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_id}&units=metric'
    response = requests.get(url).json()
    weather_data = {
        'city': city,
        'description': response['weather'][0]['description'].capitalize(),
        'temperature': round(response['main']['temp']),
        'icon': response['weather'][0]['icon']
    }
    return render_template('weather.html', weather_data=weather_data)


if __name__ == '__main__':
    app.run(debug=True)
