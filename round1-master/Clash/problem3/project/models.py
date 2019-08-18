from django.db import models
from django.contrib.auth.models import User
from django.db.models import IntegerField


class Profile(models.Model):
    p1_name = models.CharField(max_length=100)
    p2_name = models.CharField(max_length=100)
    p1_email = models.CharField(max_length=100)
    p2_email = models.CharField(max_length=100)
    mob1 = models.CharField(max_length=12)
    mob2 = models.CharField(max_length=12)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Questions(models.Model):
    question = models.CharField(max_length=500, default="")
    option1 = models.CharField(max_length=100, default="")
    option2 = models.CharField(max_length=100, default="")
    option3 = models.CharField(max_length=100, default="")
    option4 = models.CharField(max_length=100, default="")
    answer = models.CharField(max_length=100, default="")

class Score(models.Model):
    count = models.IntegerField(default=0)



