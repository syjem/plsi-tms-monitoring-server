from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from dotenv import load_dotenv

from api.services.extract import Extract

app = Flask(__name__)

CORS(app, resources={r"/api/*": {
    "origins": ["https://plsi-tms-monitoring.vercel.app"], 
    "methods": ["POST"]
}})
api = Api(app)
load_dotenv()

api.add_resource(Extract, "/api/extract")