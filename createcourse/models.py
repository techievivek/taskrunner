from django.db import models

STATUS_CHOICES=[
    (0,'Pending'),
    (1,'Success'),
    (2,'Failed')
]
# Create your models here.
class UserMap(models.Model):
    workshopUsername = models.CharField(max_length=20)
    yakshUsername = models.CharField(max_length=20)


class WorkshopCached(models.Model):
    id = models.IntegerField(primary_key=True)
    cached_time=models.DateTimeField(auto_now_add=True)
    status=models.IntegerField(choices=STATUS_CHOICES,default=0)
