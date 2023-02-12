from django.db import models


# Create your models here.

class LabInfo(models.Model):
    labName = models.CharField(max_length=30, null=False, default='labName')
    labID = models.CharField(max_length=30, null=False, default='labId')
    buildingNumber = models.IntegerField(default=0, null=False)
    floorNumber = models.IntegerField(default=0, null=False)
    numOfPcs = models.IntegerField(default=0, null=False)
    capacity = models.IntegerField(default=0, null=False)
    numOfChairs = models.IntegerField(default=0, null=False)

    def __str__(self):
        return self.labName

    class Meta:
        verbose_name = 'Laboratorie'
