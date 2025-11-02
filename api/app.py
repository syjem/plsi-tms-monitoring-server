from flask import Flask, render_template_string
from flask_cors import CORS
from flask_restful import Api
from dotenv import load_dotenv

from api import html_template, allowed_origins
from api.services.extract import Extract

app = Flask(__name__)
load_dotenv()

CORS(app, resources={r"/api/*": {
    "origins": allowed_origins, 
    "methods": ["POST"]
}})

api = Api(app)

@app.route("/")
def index():
    return render_template_string(html_template)

api.add_resource(Extract, "/api/extract")