from my_app.instrument.utils import Instrumentutils
from my_app.calendar.models import Calendar
from my_app.instrument.models import Instrument
from my_app.exchange.models import Exchange
from datetime import datetime, date
import pandas as pd

class calendarUtils(object):

    def __init__(self):
        pass

    @staticmethod
    def getCalenderforInstruments(InstrumentList):

        calendarList = Instrument.objects.filter(id__in=set(InstrumentList)).\
                        select_related('calendarid').\
                        values('exchangeid__calendar__id')

        # ToDo add code to send only unique calendafr Id
        # ToDo add code to select calendartypeid 1 for calculagtion holidays
        calendarListDF = pd.DataFrame(list(calendarList))
        calendarListDF['entrydate'] = date(1900,1,1)
        calendarListDF['exitdate'] = date(9999,1,1)
        calendarListDF['calendarid']  = calendarListDF['exchangeid__calendar__id']
        del calendarListDF['exchangeid__calendar__id']
        
        return calendarListDF
