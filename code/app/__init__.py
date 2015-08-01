from flask import Flask
import flask.ext.sqlalchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = flask.ext.sqlalchemy.SQLAlchemy(app)

