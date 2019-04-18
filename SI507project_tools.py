#__author__ == "Chen Li(chenlicl)"

#### Importing ####

# os, Flask, Flask Alchemy, populate_db.py

import os
from flask import Flask, render_template, session, redirect, url_for # tools that will make it easier to build on things
from flask_sqlalchemy import SQLAlchemy # handles database stuff for us - need to pip install flask_sqlalchemy in your virtual env, environment, etc to use this and run this
# from SI507project_tests.py import * # Import all tools available in db_populate file that I've created and saved in this directory


#### Flask app set up ####

## App Configuration ##
app = Flask(__name__)
app.debug = True
app.use_reloader = True
app.config['SECRET_KEY'] = 'hard to guess string for app security adgsdfsadfdflsdfsj'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./company_reviews.db' # TODO: decide what your new database name will be -- that has to go here
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

## Flask debug stuff ##
db = SQLAlchemy(app) # For database use
session = db.session # to make queries easy


#### Models ####
class Company(db.Model):
    __tablename__ = "companies"
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String(250), nullable = False)
    website = db.Column(db.String(250), nullable = True)
    headquater = db.Column(db.String(250), nullable = True)
    size = db.Column(db.String(250), nullable = True)
    founding_time = db.Column(db.Integer, nullable = True)
    type = db.Column(db.String(250), nullable = True)
    industry = db.Column(db.String(250), nullable = False)
    revenue = db.Column(db.String(250), nullable = True)
    ceo = db.Column(db.String(250), nullable = True)

class Review(db.Model):
    __tablename__ = "reviews"
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    company_id = db.Column(db.Integer, db.ForeignKey("companies.id"))
    location = db.Column(db.String(64), nullable = True)
    dates = db.Column(db.String(64), nullable = True)
    job_title = db.Column(db.String(250), nullable = True)
    summary = db.Column(db.String(250), nullable = True)
    pros = db.Column(db.String(250), nullable = True)
    cons = db.Column(db.String(250), nullable = True)
    advice-to-mgmt = db.Column(db.String(250), nullable = True)
    overall-rating = db.Column(db.Numeric, nullable = True)
    work-balance-rating = db.Column(db.Numeric, nullable = True)
    culture-values-rating = db.Column(db.Numeric, nullable = True)
    career-opportunity-rating = db.Column(db.Numeric, nullable = True)
    comp-benefits-rating = db.Column(db.Numeric, nullable = True)
    senior-mgmt-rating = db.Column(db.Numeric, nullable = True)
    helpful-count = db.Column(db.Integer, nullable = True)
    link = db.Column(db.String(64), nullable = True)
    companies = db.relationship('Company', backref='Review')

#### Helper function ####

## Function for calculating the most frequent words in "Pros" reviews ##

# I need a list of all Pros reviews of each company, thus 6 lists in total:
# S1 
# Each review needs to be cleaned up so that there is no "," "." and "*" before being put in the list



# Function "commom_words"
# S1: Count the frequency of each word in each string (Pro review) in that list
# S2: Find the words of the 3 greatest frequency

# Run the function "common_words" for all six lists

## S1; FIND ANd replace all , . * with space (https://www.tutorialspoint.com/python/string_replace.htm)
# str = str.replace(“,”, “ “)
# str = str.replace(“.”, “ “)
## S2: split

def workLifeBalance():




#### Routes ####

#### Initiating database ####
