#### Importing ####
## unittest
## SI507project_tools.py
import unittest
# from SI507project_tools import *
import csv

class PartOne(unittest.TestCase): # Test the downloaded csv file
    def setUp(self):
        self.file = open("employee_reviews.csv", "r")
        self.file_lines = self.file.readlines()
        # #For debug
        # print(type(self.file_lines))
        # print(len(self.file_lines[0].split(",")))
        # print(self.file_lines[0].split(",")[0])
        # print(self.file_lines[0].split(",")[1])
        self.file.close()
    def test_review_file(self): # Test whether the csv file is as described on the kaggle website
        # Test whether the records are over 67k
        self.assertTrue(len(self.file_lines) >= 67000, "Testing whether the records are over 67k.")
        # Test whether there are 17 columns as described
        self.assertTrue(len(self.file_lines[0].split(",")) == 17, "Test whether there are 17 columns as described.")

class PartTwo(unittest.TestCase): # Test modle classes

    # Test if the


if __name__ == "__main__":
    unittest.main(verbosity = 2)
    # # For debug
    # a = PartOne()
    # a.setUp()
