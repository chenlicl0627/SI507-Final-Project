from SI507project_tools import Company, Review, session
import csv

#### 1. Define the function for inserting company data ####

# company_data_file = open("company.csv", "r")
# company_data_list_of_lines = company_data_file.readlines()
# print(type(company_data_list_of_lines[1])) # this is a string type

# with open("company.csv", newline="") as csvfile:
#     reader = csv.DictReader(csvfile)
# # print(type(reader)) # this is a csv.DictReader type

def get_or_create_company(company_dic):
    company = Company.query.filter_by(name = company_dic["Company"]).first()
    if company:
        print("This company has already exists.")
        return comapny
    if not company:
        company = Company(name = company_dic["Company"], website = company_dic["Website"], headquater = company_dic["Headquater"], size=company_dic["Size"] , founding_time=company_dic["Founded"], company_type=company_dic["Type"] , industry=company_dic["Industry"], revenue=company_dic["Revenue"], ceo=company_dic["CEO"])
        session.add(company)
        session.commit

def insert_data(company_dataset):
    with open(company_dataset, newlines="") as csvfile:
        reader = csv.DictReader(csvfile)
        for line in reader:
            get_or_create_company(line)

#### 2. Define the function for inserting review data ####
