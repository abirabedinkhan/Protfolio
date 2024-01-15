from flask import render_template
from routes import app

@app.errorhandler(404)
def not_found(e):
    return "404", 404

@app.errorhandler(500)
def internal_server_error(e):
    return "500", 500