"""Route declaration."""
from flask import current_app as app
from flask import render_template

@app.route('/')
def index():
    """Landing page."""
    nav = [
        {'Math Worksheet Generator': 'Home', 'url': 'https://example.com/1'},
        {'prealgebra': 'prealgebra', 'url': 'https://example.com/2'},
        {'algebra': 'algebra', 'url': 'https://example.com/3'}
    ]
    return render_template(
        'index.html',
        nav=nav,
        title="Mathworksheets",
        description="Dynamically generates worksheets."
    )