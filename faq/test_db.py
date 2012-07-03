from db import *
import unittest
import os

TEST_DATABASE = "test.db"

CSCI3651_PREREQ = "CSCI 2911, CSCI 2912"
CSCI3651_TEXT = "Artificial Intelligence for Games"
CSCI3651_CRN = "3335"
CSCI3211_TEXT = "Engineering Long Lasting Software"
CSCI3211_CRN = "2802"
START = "Tuesday, September 4th, 2012"
END= "Sunday, December 16th, 2012"

CSCI3651 = {"name":"Game Programming","ident":"CSCI3651","textbook":CSCI3651_TEXT,"CRN":CSCI3651_CRN,"start_date":START,"end_date":END}

class TestDb(unittest.TestCase):
    def setUp(self):
      try:
         with open(TEST_DATABASE) as f: 
           os.remove(TEST_DATABASE)
           pass
      except IOError as e:
         None
    
    def test_create_table(self):
      createTable("courses", ["ident","crn","textbook","start_date","end_date"], TEST_DATABASE)
      addEntity("courses",CSCI3651, TEST_DATABASE)
      entity = grabEntity("courses",CSCI3651["ident"], TEST_DATABASE)
      self.assertEquals(entity['crn'],CSCI3651_CRN)
      self.assertEquals(entity['textbook'],CSCI3651_TEXT)
      self.assertEquals(entity['start_date'],START)

    def test_scrub(self):
      self.assertEquals("DROPTABLES",scrub("DROP TABLES --"))
      self.assertEquals("column_name",scrub("column_name"))



  
  
  
