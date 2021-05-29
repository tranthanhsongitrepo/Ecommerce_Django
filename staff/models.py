from django.db import models


# Create your models here.
class StorageStaff(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateTimeField(max_length=100)

