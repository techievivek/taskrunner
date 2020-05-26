from django.db import models

# Create your models here.
class UserMap(models.Model):
    workshopUsername=models.CharField()
    yakshUsername=models.CharField()
class WorkshopCached(models.Model):
    id=models.IntegerField()
