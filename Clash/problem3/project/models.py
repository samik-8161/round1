from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField


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
    incr = models.IntegerField(default=4)
    decr = models.IntegerField(default=2)
#    visited = ArrayField(models.IntegerField(default=0, null=True), size=100, null=True)
    buff1 = models.IntegerField(default=0)
    buff2 = models.IntegerField(default=0)
    buff3 = models.IntegerField(default=0)
    buff_cntr = models.IntegerField(default=0)
    level = models.IntegerField(default=2)

    def __str__(self):
        return self.p1_name


class Questions(models.Model):
    question = models.CharField(max_length=500, default="")
    option1 = models.CharField(max_length=100, default="")
    option2 = models.CharField(max_length=100, default="")
    option3 = models.CharField(max_length=100, default="")
    option4 = models.CharField(max_length=100, default="")
    answer = models.CharField(max_length=100, default="")
    level = models.IntegerField(default=2)

    def __str__(self):
        return self.question


class Response(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ques = models.ForeignKey(Questions, on_delete=models.CASCADE)
    resp = models.CharField(max_length=100, default="", null=True)
