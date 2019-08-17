from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    p1_name = models.CharField(max_length=100)
    p2_name = models.CharField(max_length=100,default="dummy_user")
    p1_email = models.CharField(max_length=100)
    p2_email = models.CharField(max_length=100)
    mob1 = models.CharField(max_length=12)
    mob2 = models.CharField(max_length=12)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Questions(models.Model):
    question = models.TextField(max_length=500, default="")
    attempt1 = models.TextField(blank=True, null=True)
    attempt2 = models.TextField(blank=True, null=True)
    answer = models.TextField(max_length=200, default="")