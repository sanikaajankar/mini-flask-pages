# Flask Jinja2 Dynamic Site

A multi-page web application built with Python, Flask, and Jinja2 featuring a base layout template, dynamic navigation with active route highlighting, and page-specific content blocks.

## Key Features
- **Base Template (`templates/base.html`)**: Shared layout, styling, and `{% block content %}` structure.
- **Dynamic Navigation**: Powered by a Flask `@app.context_processor` (`nav_items`) and Jinja2 `{% for %}` loop with automatic `active` state detection via `request.endpoint`.
- **Page-Specific Content**: Dynamic data rendering across Home, About, Projects, and Contact views.

## How to Run Locally
1. Install dependencies: `pip install -r requirements.txt`
2. Run the server: `python app.py`
3. Visit `http://localhost:5000/` in your browser.

