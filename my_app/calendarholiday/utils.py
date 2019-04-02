import json
from my_app.calendarholiday.models import Calendarholiday
import pandas as pd

class calendarHolidayUtils():

    def __init__(self,calendarId):
        self.calendarId = calendarId

    def getCalendarHolidays(self,startDate=None,endDate=None):

        result = None
        if startDate is None and endDate is None:

            rows = Calendarholiday.objects.filter(calendarid=self.calendarId)\
            .values('id','calendarid','name','holidaydate','modifydatetime','modifyuser')

            rows = list(rows)
            result = pd.DataFrame(rows,columns=['id','calendarid','name','holidaydate','modifydatetime','modifyuser'])

        elif startDate is not None and endDate is not None:
            
            rows = Calendarholiday.objects.filter(calendarid=self.calendarId,
            holidaydate__gte=startDate,holidaydate__lte=endDate).values('id','calendarid','name','holidaydate','modifydatetime','modifyuser')

            rows = list(rows)
            result = pd.DataFrame(rows,columns=['id','calendarid','name','holidaydate','modifydatetime','modifyuser'])
        
        return result