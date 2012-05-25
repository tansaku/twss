import unittest
from tokeniseContents import * 

class TokeniseContentsTestCase(unittest.TestCase):
    def testNumber(self): 
      self.assertEqual(tokeniseContents("Hello 1 2 3"), ['hello','number','number','number'])
    def testDollar(self):
      self.assertEqual(tokeniseContents("Hello $$$"), ['hello','dollar'])
    def testURL(self): 
      self.assertEqual(tokeniseContents("Hello http://www.google.com/search?q=hello"), ['hello','httpaddr'])
    def testEmail(self):
      self.assertEqual(tokeniseContents("Hello tansaku@gmail.com"), ['hello','emailaddr'])

if __name__ == '__main__':
     unittest.main()
