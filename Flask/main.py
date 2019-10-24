from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def main_page():
    return render_template('home.html')


@app.route('/vegetables')
def vegetables_page():
    list = ['beans', 'carrot', 'beetroot', 'cucumber']
    return render_template('vegetables.html', list=list)


@app.route('/fruits')
def fruits_page():
    list = ['melon', 'apple', 'strawberry', 'grape']
    return render_template('fruits.html', list=list)


if __name__ == "__main__":
    app.run(debug=True)
