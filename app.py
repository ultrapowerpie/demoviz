from flask import Flask, Blueprint, session, redirect, url_for, escape, request
from flask_assets import Bundle, Environment
from flask_sqlalchemy import SQLAlchemy
import os.path, zipfile, psycopg2

app = Flask(__name__)
wsgi_app = app.wsgi_app
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# = 'sqlite:///users.db'
app.secret_key = 'B4Tr98j/3yD R~XHH!jmNdL4X//3Qz'
db = SQLAlchemy(app)

from util.assets import *
from views.admin import *
from views.loci import *
from views.barcodes import *
from views.companies import *
from views.ari import *
from views.seattle import *

if not os.path.isfile("static/data/loci_activity_connections.json"):
    zip_ref = zipfile.ZipFile("static/data/data.zip", 'r')
    zip_ref.extractall("static/data/")
    zip_ref.close()

assets = Environment(app)
assets.register(bundles)

app.register_blueprint(admin)
app.register_blueprint(companies)
app.register_blueprint(barcodes)
app.register_blueprint(loci)
app.register_blueprint(ari)
app.register_blueprint(seattle)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)
