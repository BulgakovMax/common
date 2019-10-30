from flask import Flask, render_template
from utils import get_data

app = Flask(__name__)


@app.route('/')
def get_home_page():
    return render_template("home.html", data=get_data())


@app.route('/author')
def get_author_page():
    return render_template("author.html", data=get_data())


@app.route('/Alarm_clock')
def get_alarm_clock_page():
    return render_template("Alarm_clock.html", data=get_data())


@app.route('/Headphones')
def get_headphones_page():
    return render_template("Headphones.html", data=get_data())


@app.route('/IPod')
def get_ipod_page():
    return render_template("IPod.html", data=get_data())


@app.route('/Calculator')
def get_calculator_page():
    return render_template("Calculator.html", data=get_data())


@app.route('/Coffeemaker')
def get_coffemaker_page():
    return render_template("Coffeemaker.html", data=get_data())


@app.route('/Battery_charger')
def get_battery_charger_page():
    return render_template("Battery_charger.html", data=get_data())


if __name__ == "__main__":
    app.run(debug=True)
