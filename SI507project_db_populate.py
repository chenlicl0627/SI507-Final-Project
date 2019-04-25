from SI507project_tools import Company, Review, session
import csv

def get_or_create_company(company_dic):
    company = Company.query.filter_by(name = company_dic["company"]).first()
    if company:
        print("This company has already existed.")
        return company
    if not company:
        new_company = Company(name = company_dic["company"], website = company_dic["website"], headquater = company_dic["headquater"], size=company_dic["size"] , founding_time=company_dic["founded"], company_type=company_dic["type"] , industry=company_dic["industry"], revenue=company_dic["revenue"], ceo=company_dic["ceo"])
        session.add(new_company)

def insert_company_data(company_dataset):
    with open(company_dataset, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for line in reader:
            get_or_create_company(line)
        session.commit()

#### 2. Define the function for inserting review data ####

def get_or_create_review(review_dic):
    review = Review.query.filter_by(id = review_dic[""]).first()
    if review:
        print("This review has already existed.")
        return review
    if not review:
        company_name = review_dic["company"]
        company_for_new_review = Company.query.filter_by(name = company_name).first()
        new_review = Review(id=review_dic[""],location=review_dic["location"], dates=review_dic["dates"], job_title=review_dic["job-title"], summary=review_dic["summary"], pros=review_dic["pros"], cons=review_dic["cons"], advice_to_mgmt=review_dic["advice-to-mgmt"], overall_rating=review_dic["overall-ratings"], work_balance_rating=review_dic["work-balance-stars"],culture_values_rating=review_dic["culture-values-stars"], career_opportunity_rating=review_dic["carrer-opportunities-stars"], comp_benefits_rating=review_dic["comp-benefit-stars"], senior_mgmt_rating=review_dic["senior-mangemnet-stars"], helpful_count=review_dic["helpful-count"], link=review_dic["link"], company_id=company_for_new_review.id)
        session.add(new_review)

def insert_review_data(review_dataset):
    with open(review_dataset, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for line in reader:
            get_or_create_review(line)
        session.commit()

#### Initiating database ####
if __name__ == "__main__":
    pass
