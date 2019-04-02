from django.db import models

class Currency(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=3)  # Field name made lowercase.
    description = models.CharField(max_length=50)
    modifyuserid = models.ForeignKey('auth.user', models.DO_NOTHING, blank=True, null=True, db_column='ModifyUserid')  # Field name made lowercase.
    modifydatetime = models.DateTimeField(db_column='ModifyDateTime')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'currency'

    def __str__(self):
        return "Currency %s-%s" % (self.id, self.name)
