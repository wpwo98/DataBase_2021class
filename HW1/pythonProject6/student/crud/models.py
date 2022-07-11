from django.db import models

# Create your models here.
class Students(models.Model):
    sid = models.IntegerField(primary_key=True)
    sfirstname = models.CharField(max_length=25, blank=True, null=True)
    ssecondname = models.CharField(max_length=25, blank=True, null=True)
    sage = models.IntegerField(blank=True, null=True)
    smajor = models.CharField(max_length=50, blank=True, null=True)
    saddress = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.sfirstname

    class Meta:
        managed = False
        db_table = 'students'

