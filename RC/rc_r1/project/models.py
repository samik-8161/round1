from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    p1_name = models.CharField(max_length=100)
    p1_email = models.CharField(max_length=100)
    mob1 = models.CharField(max_length=12)
    p2_name = models.CharField(max_length=100, default="a")
    p2_email = models.CharField(max_length=100, default="a@a.com")
    mob2 = models.CharField(max_length=12, default="9999999999")
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="Profile")
    login_time = models.DateTimeField(null=True, max_length=100)
    logout_time = models.DateTimeField(max_length=100, null=True)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.p1_name

class Questions(models.Model):
    question = models.TextField(max_length=500, default="")
    attempt1 = models.IntegerField(blank=True, null=True)
    attempt2 = models.IntegerField(blank=True, null=True)
    answer = models.IntegerField()

    def __str__(self):
        return self.question

class Score(models.Model):
    score_cntr = models.IntegerField(default=0)