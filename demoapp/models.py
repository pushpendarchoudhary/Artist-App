from django.db import models
from django.contrib.auth.models import User


class Work(models.Model):
    LINK_CHOICES = [
        ('YT','Youtube'),
        ('IG','Instagram'),
        ('Other','Other'),
    ]
    link = models.URLField(max_length=100)
    work_type= models.CharField(max_length=10, choices=LINK_CHOICES)

class Artist(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    name= models.CharField(max_length=100)
    works=models.ManyToManyField(Work, related_name='artists')

    def __str__(self):
        return f"Artist name: {self.name}"