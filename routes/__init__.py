from flask import Flask
from libs import config
from htmlmin.main import minify
import os

template_dir = os.path.abspath('templates')
static_dir = os.path.abspath('static')
app = Flask(
    __name__, 
    template_folder = template_dir,
    static_folder = static_dir
)
app.secret_key = config.secret_key

@app.after_request
def response_minify(response):
    """
    minify html response to decrease site traffic
    """
    if response.content_type == u'text/html; charset=utf-8':
        response.set_data(
            minify(response.get_data(as_text=True))
        )

        return response
    return response

import routes.upload

import routes.errorhandler
