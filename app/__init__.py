import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS


app = Flask(__name__)
app.config.from_object('app.config.Config')

CORS(app)
cors = CORS(app, resources = {
    r"*":{
        "origins": "*"
    }
})

app_ctx = app.app_context()
app_ctx.push()

db = SQLAlchemy(app)

Migrate(app, db)
from app import views, models
