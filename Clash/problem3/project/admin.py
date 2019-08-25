from django.contrib import admin
from .models import Questions, Profile, Score, Response

admin.site.register(Questions)
admin.site.register(Profile)
admin.site.register(Score)
admin.site.register(Response)