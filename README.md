# Mini Flask Multi-Page App

A clean multi-page web application built with Python, Flask, and Jinja2 HTML templates using separate view functions for Home, About, and Contact pages.

## Routes & View Functions
- `GET /` (`home`) — Renders `templates/home.html`
- `GET /about` (`about`) — Renders `templates/about.html`
- `GET /contact` (`contact`) — Renders `templates/contact.html`

## Project Structure
- `app.py` — Flask application with dedicated view functions
- `requirements.txt` — Project dependencies (`Flask`)
- `templates/` — Jinja2 templates (`base.html`, `home.html`, `about.html`, `contact.html`)
- `README.md` — Project documentation

## How to Run Locally
1. Install dependencies: `pip install -r requirements.txt`
2. Start the server: `python app.py`
3. Visit `http://localhost:5000/` in your web browser.
