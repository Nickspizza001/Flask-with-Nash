from flask import Flask


app = Flask(__name__)

if app.config['ENV'] == 'development':
    app.config.from_object("config.DevelopmentConfig")
elif app.config['ENV'] == 'testing':
    app.config.from_object("config.TestingConfig")
else:
    app.config.from_object("config.ProductionConfig")


from app import views
from app import admin_views

from app import errors_handler