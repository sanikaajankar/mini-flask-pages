import os
from flask import Flask, render_template

app = Flask(__name__)


@app.context_processor
def inject_navigation():
    """Provide dynamic navigation items across all Jinja2 templates."""
    nav_items = [
        {"name": "Home", "endpoint": "home"},
        {"name": "About", "endpoint": "about"},
        {"name": "Projects", "endpoint": "projects"},
        {"name": "Contact", "endpoint": "contact"},
    ]
    return {"nav_items": nav_items}


@app.route('/')
def home():
    """Render the home page with dynamic context."""
    features = ["Jinja2 Template Inheritance", "Dynamic Navigation Bar", "Active Link Highlighting"]
    return render_template('home.html', title='Home', features=features)


@app.route('/about')
def about():
    """Render the about page with dynamic tech stack data."""
    tech_stack = ["Python 3", "Flask", "Jinja2", "HTML5 & CSS3"]
    return render_template('about.html', title='About', tech_stack=tech_stack)


@app.route('/projects')
def projects():
    """Render the projects page with dynamic project cards."""
    project_list = [
        {"title": "Dynamic Task Board", "desc": "Flask + SQLite app with Fetch API updates."},
        {"title": "Jinja2 Multi-Page Site", "desc": "Modular Flask templates with dynamic navigation."},
    ]
    return render_template('projects.html', title='Projects', projects=project_list)


@app.route('/contact')
def contact():
    """Render the contact page."""
    return render_template('contact.html', title='Contact', email='sanika@example.com')


if __name__ == '__main__':
    app.run(debug=os.getenv('FLASK_DEBUG', '0') == '1')
