from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SECRET_KEY']='66719af82cf7d1a7d11f3528267f3b23'

db=SQLAlchemy(app)

from . import views
from . import models