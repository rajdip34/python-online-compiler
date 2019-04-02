from django.db import models
class Index(models.Model):

    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
    currencyid = models.ForeignKey('currency.Currency', models.DO_NOTHING, db_column='CurrencyId')  # Field name made lowercase.
    bloombergticker = models.CharField(db_column='BloombergTicker', max_length=50)  # Field name made lowercase.
    reutersric = models.CharField(db_column='ReutersRic', max_length=50)  # Field name made lowercase.
    bloombergid = models.CharField(db_column='BloombergID', max_length=50)  # Field name made lowercase.
    #indextypeid = models.ForeignKey('indextype.Indextype', models.DO_NOTHING, db_column='IndexTypeId')  # Field name made lowercase.
    #indexcategoryid = models.ForeignKey('indexcategory.Indexcategory', models.DO_NOTHING, db_column='IndexCategoryId')  # Field name made lowercase.
    #indexfamilyid = models.ForeignKey('indexfamily.Indexfamily', models.DO_NOTHING, db_column='IndexFamilyId')  # Field name made lowercase.
    modifyuser = models.ForeignKey('auth.user', models.DO_NOTHING, blank=True, null=True, db_column='ModifyUserid')  # Field name made lowercase.
    modifydatetime = models.DateTimeField(db_column='ModifyDateTime')  # Field name made lowercase.
    active = models.IntegerField(db_column='Active', blank=True, null=True)  # Field name made lowercase.
    customindex = models.IntegerField(blank=True, null=True)
    customindexconfiguration = models.CharField(max_length=20000, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'index'

    def __str__(self):
        return "%s-%s" % (self.id, self.name)