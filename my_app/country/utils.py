from my_app.country.models import Country
import pandas as pd

class CountryUtils():

    def __init__(self):
        pass

    @staticmethod
    def getList():
        result = Country.objects.all().values('id', 'name').all()
        print(result)
        resultDF = pd.DataFrame(list(result),columns = ['id','name'])
        return resultDF

    def getCountryforCompany(self,company):
        rows = Instrument.objects.filter(name=company).select_related("countryid")
        """
        rows = Instrument.query\
        .join(Country, Country.id==Instrument.countryid)\
        .filter(Instrument.name == company)\
        .with_entities(Country.name).all()
        """
        return rows