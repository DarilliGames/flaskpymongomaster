import os
from flask import Flask, render_template, redirect, url_for, request
from flask_paginate import Pagination, get_page_args
from bson.objectid import ObjectId
from flask_pymongo import PyMongo

development = True

if development:
    import env


app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'testerMongo'
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')
app.secret_key = 'some_secret'

mongo = PyMongo(app)




if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)