from django.db import models


# Create your models here.

class Report(models.Model):
    labID = models.CharField(max_length=30, null=False)
    date = models.DateField('%m/%d/%Y', null=False)
    type = models.CharField(max_length=10, null=False)
    problem = models.CharField(max_length=1500)

    class Meta:
        verbose_name = 'report'
