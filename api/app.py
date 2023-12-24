from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_random_color')
def get_random_color():
    random_color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
    return {'random_color': random_color}

@app.route('/get_random_even_number')
def get_random_even_number():
    random_even_number = random.randrange(1, 5000000) * 2
    return {'random_even_number': random_even_number}

if __name__ == '__main__':
    app.run(debug=True)
