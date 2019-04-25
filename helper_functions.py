from stopwords import stopword_list
import nltk # Need to install NLTK in virtual env: pip install -U nltk
from nltk.tokenize import word_tokenize
import string

#### Helper function ####

## Functions for calculating the most frequent words in "Pros" and "Cons" reviews ##

def remove_punctuation_stopwords(review_str):
    stop_words = set(stopword_list)
    lower_case_review_str = review_str.lower()
    word_tokens = word_tokenize(lower_case_review_str)
    review_no_stop_words_punct = [item for item in word_tokens if item not in stop_words and item not in string.punctuation]
    return review_no_stop_words_punct
    ## Reference: https://stackoverflow.com/questions/45516207/removing-stop-words-and-string-punctuation


def frequent_word(review_list):
	count_dic = {}
	# Count the word frequency in each filtered review
	for review in review_list:
		filtered_review_wd_list = remove_punctuation_stopwords(review) ## this would be a list
		for word in filtered_review_wd_list:
			if word not in count_dic:
				count_dic[word] = 1
			else:
				count_dic[word] += 1
    # Find the most frequent word
	largenum = 0
	most_frequent_word = ''
	for key in count_dic:
		if count_dic[key] > largenum:
			largenum = count_dic[key]
			most_frequent_word = key
		elif count_dic[key] == largenum:
			largenum = count_dic[key]
			most_frequent_word = most_frequent_word + ' AND ' + key
	return most_frequent_word

def get_pros_review_list(review_list):
    for review in review_list:
        pros_review_list = []
        a_pros_review = review.pros
        if a_pros_review:
            pros_review_list.append(a_pros_review)
        return pros_review_list

def get_cons_review_list(review_list):
    for review in review_list:
        cons_review_list = []
        a_cons_review = review.cons
        if a_cons_review:
            cons_review_list.append(a_cons_review)
        return cons_review_list

## Functions for calculating the average work-life balance rating for each company ##

def get_work_life_balance_rating_list(review_list):
    for review in review_list:
        work_life_balance_rating_list = []
        a_work_life_balance_rating = review.work_balance_rating
        if a_work_life_balance_rating:
            work_life_balance_rating_list.append(a_work_life_balance_rating)
        return work_life_balance_rating_list

def average_rating (rating_list):
    total_num = 0
    count = 0
    for rating in rating_list:
        total_num = total_num + float(rating)
        count += 1
    result = total_num/count
    return result
