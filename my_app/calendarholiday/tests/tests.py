import unittest
from datetime import datetime, timedelta, date
import decimal

from django.test import Client
from my_app.calendarholiday.models import Calendarholiday
from my_app.calendarholiday.utils import calendarHolidayUtils
import pandas as pd


class SimpleTest(unittest.TestCase):
    def setUp(self):
        # Every test needs a client.
        # self.client = Client()
        pass

    def test_checkFields(self):
        print("Calendar Holiday : check fields")
        _calendarHoliday = Calendarholiday.objects.filter(id=2166)
        self.assertEqual(_calendarHoliday[0].name,'Christmas - Early close at 14:00')
        self.assertEqual(_calendarHoliday[0].holidaydate.strftime('%m/%d/%Y'),'12/24/2010')
        self.assertEqual(_calendarHoliday[0].modifyuser.id, 1)


    def test_checkInstance(self):
        print('Calendar Holiday : check instance')
        _calendarHolidayUtilsObj = calendarHolidayUtils(23)
        self.assertEqual(True, isinstance(_calendarHolidayUtilsObj, calendarHolidayUtils))


    def test_getCalendarHolidays(self):
        print('Calendar Holiday : check getCalendarHoliday')
        _calendarHolidayUtilsObj = calendarHolidayUtils(23)
        resultFrame = _calendarHolidayUtilsObj.getCalendarHolidays('2012-12-25','2015-12-31')

        resultFramerows = resultFrame.loc[(resultFrame['calendarid']== 23 ) & (resultFrame['holidaydate']==date(2012,12,25))]
        resultFramerow = resultFramerows.iloc[0]
        self.assertEqual('Christmas', resultFramerow['name'])

        resultFramerows = resultFrame.loc[(resultFrame['calendarid']== 23 ) & (resultFrame['holidaydate']==date(2010,12,25))]
        self.assertEqual(0,len(resultFramerows))


        resultFramerows = resultFrame.loc[(resultFrame['calendarid']== 23 ) & (resultFrame['holidaydate']==date(2016,12,25))]
        self.assertEqual(0,len(resultFramerows))



    def test_getCalendarHolidays(self):
        print('Calendar Holiday : check getCalendarHoliday')
        _calendarHolidayUtilsObj = calendarHolidayUtils(23)
        resultFrame = _calendarHolidayUtilsObj.getCalendarHolidays()

        resultFramerows = resultFrame.loc[(resultFrame['calendarid']== 23 ) & (resultFrame['holidaydate']==date(2012,12,25))]
        resultFramerow = resultFramerows.iloc[0]
        self.assertEqual('Christmas', resultFramerow['name'])

        resultFramerows = resultFrame.loc[(resultFrame['calendarid']== 23 ) & (resultFrame['holidaydate']==date(2010,12,24))]
        self.assertEqual(1,len(resultFramerows))


        resultFramerows = resultFrame.loc[(resultFrame['calendarid']== 23 ) & (resultFrame['holidaydate']==date(2015,12,25))]
        self.assertEqual(1,len(resultFramerows))


    def test_getCalendarHolidays_2(self):
        print('Calendar Holiday : check getCalendarHoliday')
        _calendarHolidayUtilsObj = calendarHolidayUtils(45)
        resultFrame = _calendarHolidayUtilsObj.getCalendarHolidays('1900-01-01','2012-12-31')

        print(resultFrame)

        # resultFramerows = resultFrame.loc[(resultFrame['calendarid']== 23 ) & (resultFrame['holidaydate']==date(2012,12,25))]
        # resultFramerow = resultFramerows.iloc[0]
        # self.assertEqual('Christmas', resultFramerow['name'])

        # resultFramerows = resultFrame.loc[(resultFrame['calendarid']== 23 ) & (resultFrame['holidaydate']==date(2010,12,24))]
        # self.assertEqual(1,len(resultFramerows))


        # resultFramerows = resultFrame.loc[(resultFrame['calendarid']== 23 ) & (resultFrame['holidaydate']==date(2015,12,25))]
        # self.assertEqual(1,len(resultFramerows))