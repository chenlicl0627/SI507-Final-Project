# Project Title

What employees say about Big Tech?

[Link to this repository](https://github.com/chenlicl0627/SI507-Final-Project)

---

## Project Description

This should be a brief description of what your project is and does.
This program does some simple analysis on the data of employee reviews for the six big technology companies, Google, Amazon, Apple, Microsoft Facebook and Netflix, between 2008 and 2018 on Glassdoor, and show the analysis result in graphics and text.

## How to run

1. First, you should install all requirements:

Make sure you have `virtualenv` installed. If you don't, use the following command to install `virtualenv`:

> pip install virtualenv

Then, `cd` to the project directory and activate `virtualenv`:

> source venv/bin/activate

Then, you can install this project's dependencies:

> pip install -r requirements.txt

2. Second, you should run `python SI507project_tools.py runserver`.


3. Only run `insert_company_data("company.csv")` and `insert_review_data("employee_reviews.csv")` at the end of the "SI507project_tools.py" file if the population of the database is necessary -- becasue it takes a while! If it's already been done, and .db/sqlite file exists, comment it out.

## How to use

1. A useful instruction goes here
2. A useful second step here
3. (Optional): Markdown syntax to include an screenshot/image: ![alt text](image.jpg)

## Routes in this application
- `/commonwords` -> this is a page for users to see the most frequent three words in the reviews regarding each company’s “pros” or “cons” based on user selection (e.g. there will be a toggle button for pro/con).
- `/worklifebalance` -> this is a page for users to learn about each company’s work&life balance rating through bar charts.
- `/result` -> this is a page for users to see the overall rating difference between current employees and former employees.

## How to run tests (leave this for next time)
1. First... (e.g. access a certain directory if necessary)
2. Second (e.g. any other setup necessary)
3. etc (e.g. run the specific test file)
NOTE: Need not have 3 steps, but should have as many as are appropriate!

## In this repository:
- SI507project_tools.py
- SI507project_db-populate.py
- SI507project_tests.py
- company.csv
- employee_reviews.csv
- templates
  - commonWords.html
  - workLifeBalance.html
  - current-FormerComparison.html
- requirements.txt
- Employee Review Database Diagram.png

---
## Code Requirements for Grading
Please check the requirements you have accomplished in your code as demonstrated.
- [x] This is a completed requirement.
- [ ] This is an incomplete requirement.

Below is a list of the requirements listed in the rubric for you to copy and paste.  See rubric on Canvas for more details.

### General
- [ ] Project is submitted as a Github repository
- [ ] Project includes a working Flask application that runs locally on a computer
- [x] Project includes at least 1 test suite file with reasonable tests in it.
- [ ] Includes a `requirements.txt` file containing all required modules to run program
- [x] Includes a clear and readable README.md that follows this template
- [ ] Includes a sample .sqlite/.db file
- [x] Includes a diagram of your database schema
- [ ] Includes EVERY file needed in order to run the project
- [ ] Includes screenshots and/or clear descriptions of what your project should look like when it is working

### Flask Application
- [x] Includes at least 3 different routes
- [x] View/s a user can see when the application runs that are understandable/legible for someone who has NOT taken this course
- [x] Interactions with a database that has at least 2 tables
- [x] At least 1 relationship between 2 tables in database
- [x] Information stored in the database is viewed or interacted with in some way

### Additional Components (at least 6 required)
- [ ] Use of a new module
- [ ] Use of a second new module
- [ ] Object definitions using inheritance (indicate if this counts for 2 or 3 of the six requirements in a parenthetical)
- [ ] A many-to-many relationship in your database structure
- [ ] At least one form in your Flask application
- [ ] Templating in your Flask application
- [ ] Inclusion of JavaScript files in the application
- [ ] Links in the views of Flask application page/s
- [ ] Relevant use of `itertools` and/or `collections`
- [ ] Sourcing of data using web scraping
- [ ] Sourcing of data using web REST API requests
- [x] Sourcing of data using user input and/or a downloaded .csv or .json dataset
- [ ] Caching of data you continually retrieve from the internet in some way

### Submission
- [ ] I included a link to my GitHub repository with the correct permissions on Canvas! (Did you though? Did you actually? Are you sure you didn't forget?)
- [ ] I included a summary of my project and how I thought it went **in my Canvas submission**!
