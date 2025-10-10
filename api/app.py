import os
from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from dotenv import load_dotenv

from api.services.extract import Extract

app = Flask(__name__)
load_dotenv()

allowed_origins = ["https://plsi-tms-monitoring.vercel.app"]
if (os.getenv("FLASK_ENV") == 'development'):
    allowed_origins.append("http://localhost:3000/")

CORS(app, resources={r"/api/*": {
    "origins": allowed_origins, 
    "methods": ["POST"]
}})
api = Api(app)

api.add_resource(Extract, "/api/extract")