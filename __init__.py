from flask import Flask
from flask_cors import Cors
from flask_mongokit import MongoKit

from home.mongo_rest.home.documents import Home

app = Flask(__name__)

app.config['SECRET_KEY'] = 'SECRET_KEY'
app.config['MONGODB_DATABASE'] = "/test"

CORS(app, resources={r"/api/*": {"origins": "*"}})
db = MongoKit(app)

db.register([Home])

from home.mongo_rest.home.api import home_api
app.register_blueprint(home_api, url_prefix="/api/v1")
