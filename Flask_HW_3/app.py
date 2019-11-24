from datetime import timedelta

from flask import Flask, render_template
from blueprints.products.main import product
from blueprints.supermarkets.main import supermarket

app = Flask(__name__)
app.config['SECRET_KEY'] = 'very_secret_key'
app.register_blueprint(supermarket)
app.register_blueprint(product)



app.config['SESSION_TYPE'] = 'filesystem'
app.permanent_session_lifetime = timedelta(seconds=30)


@app.route("/")
def get_home_page():
    return render_template("home.html", title='HOME')


@app.errorhandler(404)
def get_error_page(error):
    return render_template("404.html", title='404 ERROR')


if __name__ == "__main__":
    app.run(debug=True)
