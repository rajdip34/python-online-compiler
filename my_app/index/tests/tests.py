import unittest
import datetime

from django.test import Client

from my_app.index.models import Index

class SimpleTest(unittest.TestCase):
    def setUp(self):
        # Every test needs a client.
        #self.client = Client()
        pass

    def test_checkFields(self):
        # Issue a GET request.
        #response = self.client.get('/login/')

        # Check that the response is 200 OK.
        #self.assertEqual(response.status_code, 200)
        print("Running Index get fields...")
        index = Index.objects.filter(id=2)
        self.assertEqual(index[0].name,"Test")
        self.assertEqual(index[0].currencyid.id,2)
        self.assertEqual(index[0].bloombergticker,"Ticker1")
        self.assertEqual(index[0].reutersric,"Ric1")
        self.assertEqual(index[0].bloombergid,"300")
        self.assertEqual(index[0].indextypeid.id,1)
        self.assertEqual(index[0].indexcategoryid.id,1)
        self.assertEqual(index[0].indexfamilyid.id,1)
        self.assertEqual(index[0].modifyuser.id,1)
        self.assertEqual(index[0].modifydatetime.strftime('%m/%d/%Y'),"05/02/2016")
        self.assertEqual(index[0].active,0)
        self.assertEqual(index[0].customindex,0)
        self.assertEqual(index[0].customindexconfiguration,"")

    
    def test_checkInsertion(self):

        pass
  
