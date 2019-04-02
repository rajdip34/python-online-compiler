from django.db import models

class Calendarholiday(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    calendarid = models.ForeignKey('calendar.Calendar', models.DO_NOTHING, db_column='CalendarID')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
    holidaydate = models.DateField(db_column='HolidayDate')  # Field name made lowercase.
    modifyuser = models.ForeignKey('auth.user', models.DO_NOTHING, blank=True, null=True, db_column='ModifyUserid')  # Field name made lowercase.
    modifydatetime = models.DateTimeField(db_column='ModifyDateTime')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'calendarholiday'
        unique_together = (('calendarid', 'holidaydate'),)

    def __str__(self):
        return "%s-%s" % (self.id, self.name)