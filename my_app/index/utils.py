from my_app.index.models import Index


class indexUtils(object):

    def __init__ (self,indexid, user_id):
        self.id = indexid
        self.user_id = user_id
    
    def getDetails(self):
        result = Index.objects.get(id=self.id)
        return (result)
        
    @staticmethod
    def createIndex(name,currencyid,bloombergticker,reutersric,bloombergid,indextypeid,indexcategoryid,indexfamilyid,modifyuserid,modifydatetime,active,customindex,customindexconfiguration):

        row = Index.objects.filter(name=name)

        if not row.exists():
            _newIndex = Index.objects.create(name=name,currencyid=currencyid,
                              bloombergticker=bloombergticker,
                              reutersric=reutersric,
                              bloombergid=bloombergid,
                              indextypeid=indextypeid,
                              indexcategoryid=indexcategoryid,
                              indexfamilyid=indexfamilyid,
                              modifyuser=modifyuserid,
                              modifydatetime=modifydatetime,
                              active=active,
                              customindex=customindex,
                              customindexconfiguration=customindexconfiguration)

            return _newIndex.id
        else:
            return row[0].id

    def getDataforHomePage(self):
        index_data = Index.objects.filter(active=1, indexuserpermission__userid=self.user_id).select_related(
            'currencyid', 'indexfamilyid','indexcategoryid', 'indextypeid')
        data_list = []
        if index_data:
            for i in index_data:
                data_dict = dict()
                data_dict['id']= i.id
                data_dict['name'] = i.name
                data_dict['currency'] = i.currencyid.name if i.currencyid else "-"
                data_dict['family'] = i.indexfamilyid.name if i.indexfamilyid else "-"
                data_dict['category'] = i.indexcategoryid.name if i.indexcategoryid else "-"
                data_dict['type'] = i.indextypeid.name if i.indextypeid else "-"
                data_dict['modifydatetime'] = i.name
                data_dict['modifyuserid'] = i.modifyuser_id
                data_list.append(data_dict)
        """
        data = Index.query\
        .join(Indexcategory, Indexcategory.id == Index.indexcategoryid)\
        .join(Indexfamily, Indexfamily.id == Index.indexfamilyid)\
        .join(Indextype, Indextype.id == Index.indextypeid)\
        .join(Currency, Currency.id == Index.currencyid)\
        .join(Indexuserpermission, Indexuserpermission.indexid== Index.id)\
        .filter(Index.active==1 , Indexuserpermission.userid == int(current_user.get_id()) )\
        .with_entities(Index.id, Index.name, Currency.name.label('currency') , Indexfamily.name.label('family'),
                       Indexcategory.name.label('category'), Indextype.name.label('type'), Index.modifydatetime, Index.modifyuserid).all()
        print(data)
        return (data)
        """
        return data_list


    def getDataforHomePageCustom(self):
        """
        data = Index.query\
        .join(Indexcategory, Indexcategory.id == Index.indexcategoryid)\
        .join(Indexfamily, Indexfamily.id == Index.indexfamilyid)\
        .join(Indextype, Indextype.id == Index.indextypeid)\
        .join(Currency, Currency.id == Index.currencyid)\
        .join(Indexuserpermission, Indexuserpermission.indexid== Index.id)\
        .filter(Index.active==1 , Indexuserpermission.userid == int(current_user.get_id()), Index.customindex==1 )\
        .with_entities(Index.id, Index.name, Currency.name.label('currency') , Indexfamily.name.label('family'), Indexcategory.name.label('category'), Indextype.name.label('type'), Index.modifydatetime, Index.modifyuserid).all()
        print(data)
        return (data)s
        """
        index_data = Index.objects.filter(active=1, indexuserpermission__userid=self.user_id,
                                          customindex=1).select_related(
            'currencyid', 'indexfamilyid', 'indexcategoryid', 'indextypeid')
        data_list = []
        if index_data:
            for i in index_data:
                data_dict = dict()
                data_dict['id'] = i.id
                data_dict['name'] = i.name
                data_dict['currency'] = i.currencyid.name if i.currencyid else "-"
                data_dict['family'] = i.indexfamilyid.name if i.indexfamilyid else "-"
                data_dict['category'] = i.indexcategoryid.name if i.indexcategoryid else "-"
                data_dict['type'] = i.indextypeid.name if i.indextypeid else "-"
                data_dict['modifydatetime'] = i.name
                data_dict['modifyuserid'] = i.modifyuser_id
                data_list.append(data_dict)
        return data_list

    def getInputs(self,formData):

        # industry = {"industry":["Oil & Gas","Basic Materials"]}
        # sector = {"sector":["Leisure Goods"]}
        # subsector = {"subsector":["Aerospace"]}
        # supersector = {"supersector":["Health Care"]}
        # country = {"country":["Turkey","France","Germany","United Kingdom"]}
        # marketCap = {"marketCap":{"weight":1.0,"HigherTheBetter":True}}
        # vol={"vol":{"weight":0.0,"HigherTheBetter":True}}
        # momentum={"momentum":{"weight":0.0,"HigherTheBetter":False}}
        # stockSelection ={"stockSelection":{"TopOrBottom":request.form["TopOrBottom"], "number":int(request.form["numberofstocks"])}}

        # combinedInput = {}
        # combinedInput["nonQuantitativrFactor"] = [industry,sector,subsector,supersector,country]
        # combinedInput["quantitativeFactor"]=[marketCap,vol,momentum]
        # combinedInput["stockSelection"]=[stockSelection]
        # combinedInput["weightMethod"]=request.form["weight"]
        # combinedInput["maxWeight"]= 10
        # combinedInput["rebalanceFrequency"]=request.form["rebalanceFrequency"]
        # combinedInput["backtestPeriod"]= int(period)
        # combinedInput["startDate"]=request.form["startdate"]
        # combinedInput["currency"]=request.form["currency"]
        # if 'stage1-category-0' in formData.keys():
        #     industry = formData['stage1-category-1']
        pass
