from django.db import models

STATUS_CHOICES = [(0, 'Pending'), (1, 'Success'), (2, 'Failed')]


# Create your models here.
class UserMap(models.Model):
    workshop_user = models.CharField(max_length=20)
    yaksh_user = models.CharField(max_length=20)


class WorkshopCached(models.Model):
    workshop_id = models.IntegerField()
    cached_time = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=0) #refer above CHOICES
