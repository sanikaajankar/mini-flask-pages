import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    """Render the home page view."""
    return render_template('home.html', title='Home')


@app.route('/about')
def about():
    """Render the about page view."""
    return render_template('about.html', title='About')


@app.route('/contact')
def contact():
    """Render the contact page view."""
    return render_template('contact.html', title='Contact')


if __name__ == '__main__':
    app.run(debug=os.getenv('FLASK_DEBUG', '0') == '1')
