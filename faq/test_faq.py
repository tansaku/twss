from faq import *
import unittest
from test_db import *

class TestFaq(unittest.TestCase):
  def setUp(self):
    try:
       with open(TEST_DATABASE) as f: 
         os.remove(TEST_DATABASE)
         pass
    except IOError as e:
       None
       
  def test(self):
    result = ""
    aspects = aspectList.keys()
    for course in courses:
      for aspect in aspects:
        result += humanizedQuestion(course,aspect) + "\n"
    self.assertEqual(query("What's the CRN of CSCI3651"),"The CRN for CSCI3651 is '3335'")
    self.assertEqual(query("What's the textbook of Systems Analysis?"),"The textbook for CSCI3211 is 'Engineering Long Lasting Software'")
    self.assertEqual(query("what's the CRN for Systems Analysis"),"The CRN for CSCI3211 is '2802'")
    self.assertEqual(query("What's the start date of 3651"),"The start date for CSCI3651 is 'Tuesday, September 4th, 2012'")
    #self.assertEqual(query("So, what are you wearing?"),"Does this help? http://uk.gamespot.com/the-elder-scrolls-v-skyrim/forum/so-what-are-you-wearing-63261933/")

  def testCreation(self):
    ''' test we can create and modify arbitrary entities '''
    process("There is a course CSCI4702 called Mobile Programming", TEST_DATABASE)
    entity = grabEntity("courses", "CSCI4702", TEST_DATABASE)
    self.assertEquals(entity['name'],"Mobile Programming")
    self.assertEquals(entity['ident'],"CSCI4702")
    process("CSCI4702 has a start date of Jan 31st 2013", TEST_DATABASE)
    entity = grabEntity("courses", "CSCI4702", TEST_DATABASE)
    self.assertEquals(entity['start_date'],"Jan 31st 2013")
    self.assertEquals(entity['name'],"Mobile Programming")
    self.assertEquals(entity['ident'],"CSCI4702")
    
  def testOtherCreation(self):
    ''' test we can create and modify arbitrary entities '''
    process("There is a professor Sam Joseph called Sam", TEST_DATABASE)
    entity = grabEntity("professors", "Sam Joseph", TEST_DATABASE)
    self.assertEquals(entity['name'],"Sam")
    self.assertEquals(entity['ident'],"Sam Joseph")
    process("Sam Joseph has a birth date of May 13th 1972", TEST_DATABASE)
    entity = grabEntity("professors", "Sam Joseph", TEST_DATABASE)
    self.assertEquals(entity['birth_date'],"May 13th 1972")
    self.assertEquals(entity['name'],"Sam")
    self.assertEquals(entity['ident'],"Sam Joseph")

  

  


  
  
  
