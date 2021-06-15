from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from .config import Config
from asgiref.wsgi import WsgiToAsgi
# all major dependencies are defiend here itself maintaining modularity

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
api_key = app.config['YOUTUBE_DATA_API_KEY']
asgi_app = WsgiToAsgi(app)

# avoiding circular imports
from . import routes, models