import unittest
from datetime import datetime, timedelta, date
import decimal

from django.test import Client
from my_app.calendar.utils import calendarUtils
import pandas as pd


class SimpleTest(unittest.TestCase):
    def setUp(self):
        # Every test needs a client.
        # self.client = Client()
        pass


    def test_getCalenderforInstruments(self):
        print('check getCalenderforInstruments')

        CalendarUtilObj = calendarUtils()
        resultFrame = CalendarUtilObj.getCalenderforInstruments([4460,4461,4462])
        # print(resultFrame)
        calendar = resultFrame.loc[(resultFrame['calendarid'] == 24 )]
        
        # print(calendarid)
        self.assertEqual(len(calendar)==1,True)
        # print(resultFrame)









