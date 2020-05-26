from django.db import models


# Create your models here.
class UserMap(models.Model):
    workshopUsername = models.CharField(max_length=20)
    yakshUsername = models.CharField(max_length=20)


class WorkshopCached(models.Model):
    id = models.IntegerField(primary_key=True)
