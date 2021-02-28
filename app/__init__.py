from flask import Flask
from .config import Config
from flask_wtf.csrf import CSRFProtect

csrf = CSRFProtect()

app = Flask(__name__)
app.config.from_object(Config)


from app import views
csrf.init_app(app)