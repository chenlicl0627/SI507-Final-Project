#__author__ == "Chen Li(chenlicl)"

#### Importing ####

import os
from flask import Flask, render_template, session, redirect, url_for, request # tools that will make it easier to build on things
from flask_sqlalchemy import SQLAlchemy # handles database stuff for us - need to pip install flask_sqlalchemy in your virtual env, environment, etc to use this and run this
from SI507project_db_populate import *
from helper_functions import *

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
    company_type = db.Column(db.String(250), nullable = True)
    industry = db.Column(db.String(250), nullable = False)
    revenue = db.Column(db.String(250), nullable = True)
    ceo = db.Column(db.String(250), nullable = True)

class Review(db.Model):
    __tablename__ = "reviews"
    id = db.Column(db.Integer, primary_key = True)
    location = db.Column(db.String(64), nullable = True)
    dates = db.Column(db.String(64), nullable = True)
    job_title = db.Column(db.String(250), nullable = True)
    summary = db.Column(db.String(250), nullable = True)
    pros = db.Column(db.String(250), nullable = True)
    cons = db.Column(db.String(250), nullable = True)
    advice_to_mgmt = db.Column(db.String(250), nullable = True)
    overall_rating = db.Column(db.String(250), nullable = True)
    work_balance_rating = db.Column(db.String(250), nullable = True)
    culture_values_rating = db.Column(db.String(250), nullable = True)
    career_opportunity_rating = db.Column(db.String(250), nullable = True)
    comp_benefits_rating = db.Column(db.String(250), nullable = True)
    senior_mgmt_rating = db.Column(db.String(250), nullable = True)
    helpful_count = db.Column(db.Integer, nullable = True)
    link = db.Column(db.String(64), nullable = True)
    company_id = db.Column(db.Integer, db.ForeignKey("companies.id"))
    company = db.relationship('Company')


#### Routes ####

## Route 1 - homepage ##

@app.route("/")
def greeting():
    return render_template('homepage.html')

## Route 2 - finding the most frequent word used in the pros/cons reviews for each company ##

@app.route('/choose_pros_or_cons')
def pros_or_cons_form():
    return render_template('pros_or_cons_form.html')

@app.route("/themostfrequentwords", methods=["GET"])
def see_frequent_words():
    user_choice = request.args.get("review_type")
    company_index_list = [1,2,3,4,5,6]
    if user_choice == "pros":
        company_word_tuple_list = []
        for i in company_index_list:
            company = Company.query.filter_by(id=i).first()
            company_name_lowercase = company.name
            company_name_uppercase =company_name_lowercase.upper()
            company_review_list = Review.query.filter_by(id=i).all()
            company_pros_review_list = get_pros_review_list(company_review_list)
            company_pros_frequent_word = frequent_word(company_pros_review_list)
            company_word_tuple = (company_name_uppercase, company_pros_frequent_word)
            company_word_tuple_list.append(company_word_tuple)
        return render_template('frequent_words.html', company_word_list = company_word_tuple_list, review_type = user_choice)
    if user_choice == "cons":
        company_word_tuple_list = []
        for i in company_index_list:
            company_name_lowercase = Company.query.filter_by(id=i).first().name
            company_name_uppercase =company_name_lowercase.upper()
            company_review_list = Review.query.filter_by(id=i).all()
            company_cons_review_list = get_cons_review_list(company_review_list)
            company_cons_frequent_word = frequent_word(company_cons_review_list)
            company_word_tuple = (company_name_uppercase, company_cons_frequent_word)
            company_word_tuple_list.append(company_word_tuple)
        return render_template('frequent_words.html', company_word_list = company_word_tuple_list, review_type = user_choice)

## Route 3 - displaying the average work-life balance rating for each company ##

@app.route("/work_life_balance")
def see_work_life_balance_rating():
    # Get a list of work_life_balance rating for each company_id
    company_index_list = [1,2,3,4,5,6]
    company_rating_tuple_list = []
    for i in company_index_list:
        company_review_list = Review.query.filter_by(id=i).all()
        company_work_life_balance_rating_list = get_work_life_balance_rating_list(company_review_list)
        # Calculate the average rating with the average_rating() function
        company_average_work_life_balance_rating = average_rating(company_work_life_balance_rating_list)
        # Put the company name and the rating in a tuple
        company_name_lowercase = Company.query.filter_by(id=i).first().name
        company_name_uppercase = company_name_lowercase.upper()
        company_rating_tuple = (company_name_uppercase, company_average_work_life_balance_rating)
        company_rating_tuple_list.append(company_rating_tuple)
    # Display the average rating for each company
    return render_template('work_life_balance.html', company_rating_list = company_rating_tuple_list)

if __name__ == "__main__":

    # Populate database - IMPORTANT: Please comment out the following three lines of code once the database is populated.
    db.create_all()
    insert_company_data("company.csv")
    insert_review_data("employee_reviews.csv")

    # Initiate Flask app - - IMPORTANT: Please uncomment the following code once the database is populated.
    # app.run() # run with this: python3 SI507project_tools.py runserver
