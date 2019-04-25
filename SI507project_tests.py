#### Importing ####

import unittest
from helper_functions import *
import csv

class PartOne(unittest.TestCase): # Test the downloaded csv file
    def setUp(self):
        self.file = open("employee_reviews.csv", "r")
        self.file_lines = self.file.readlines()
        self.file.close()

    def test_review_file(self): # Test whether the csv file is as described on the kaggle website
        # Test whether the records are over 67k
        self.assertTrue(len(self.file_lines) >= 67000, "Testing whether the records are over 67k.")

    def test_review_file_header(self): # Test whether the csv file is as described on the kaggle website
        # Test whether there are 17 columns as described
        self.assertTrue(len(self.file_lines[0].split(",")) == 17, "Test whether there are 17 columns as described.")

class PartTwo(unittest.TestCase): # Test the function that removes punctuation and stopwords from each review string.
    def test_filtering_result_filtered_string(self):
        review_str1= "- A company culture that encourages dissent, discourse, transparency, and fairness - Strong compensation, from benefits, to perks, to base pay - Decent internal mobility opportunities - Employees are ..."
        filtering_result1 = remove_punctuation_stopwords(review_str1)
        self.assertTrue("-" not in filtering_result1)
        self.assertTrue("," not in filtering_result1)
        self.assertTrue("." not in filtering_result1)
        review_str2= "* If you're a software engineer, you're among the kings of the hill at Google. It's an engineer-driven company without a doubt (that *is* changing, but it's still very engineer-focused). * The perks a..."
        filtering_result2 = remove_punctuation_stopwords(review_str2)
        self.assertTrue("*" not in filtering_result2)
        self.assertTrue("(" not in filtering_result2)
        self.assertTrue("you're" not in filtering_result2)

    def test_filtering_result_kept_string(self):
        review_str1= "- A company culture that encourages dissent, discourse, transparency, and fairness - Strong compensation, from benefits, to perks, to base pay - Decent internal mobility opportunities - Employees are ..."
        filtering_result1 = remove_punctuation_stopwords(review_str1)
        self.assertTrue("company" in filtering_result1)
        self.assertTrue("transparency" in filtering_result1)
        self.assertTrue("benefits" in filtering_result1)
        review_str2= "* If you're a software engineer, you're among the kings of the hill at Google. It's an engineer-driven company without a doubt (that *is* changing, but it's still very engineer-focused). * The perks a..."
        filtering_result2 = remove_punctuation_stopwords(review_str2)
        self.assertTrue("software" in filtering_result2)
        self.assertTrue("engineer" in filtering_result2)
        self.assertTrue("kings" in filtering_result2)
        self.assertTrue("engineer-driven" in filtering_result2)

if __name__ == "__main__":
    unittest.main(verbosity = 2)
