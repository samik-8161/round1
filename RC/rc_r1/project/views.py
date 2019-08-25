import datetime
import random
import re

from django.contrib import auth
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login, logout

from .models import Questions, Profile, Score

regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'


def index1(request):
    if request.method == "POST":
        if request.POST['pass'] == request.POST['passwordagain']:
            try:
                user = User.objects.get(username=request.POST['uname'])
                return render(request, 'signup.html', {'error': "Username Has Already Been Taken"})
            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST['uname'], password=request.POST['pass'])
                p1_name = request.POST['p1_name']
                p1_email = request.POST['p1_email']
                mob1 = request.POST['mob1']
                p2_name = request.POST['p2_name']
                p2_email = request.POST['p2_email']
                mob2 = request.POST['mob2']

                userprofile = Profile(p1_name=p1_name, p1_email=p1_email, mob1=mob1, p2_name=p2_name, p2_email=p2_email,
                                      mob2=mob2, user=user)

            if re.search(regex, p1_email and p2_email):
                auth.login(request, user)
                userprofile.login_time = datetime.datetime.now(login(request, user))
                userprofile.save()
                return redirect(reverse('index2'))
            else:
                return render(request, 'signup.html', {'error': "Email not valid"})
        else:
            return render(request, 'signup.html', {'error': "Passwords Don't Match"})
    else:
        return render(request, 'signup.html')


def index2(request):
    profile = request.user.Profile
    qno = random.randint(1, 5)
    questions = Questions.objects.get(pk=qno)
    print(profile.score)
    context = {'question': questions, 'score': profile.score}
    return render(request, 'Question.html', context)


def index3(request, qno):
    profile = Profile.objects.get(user=request.user)
    answer = Questions.objects.get(pk=qno)
    a = Score.objects.get(pk=1).score_cntr
    b = Score.objects.get(pk=2).score_cntr
    c = Score.objects.get(pk=3).score_cntr
    ans1 = request.POST.get('attempt1')
    if answer.answer == ans1:
        profile.score = profile.score + a
        return redirect(reverse('index2'))
    else:
        ans2=request.POST.get('attempt2')
        if answer.answer == ans2:
            profile.score = profile.score - b
        else:
            profile.score = profile.score - c
    profile.save()
    return redirect(reverse('index2'))


def index4(request):
    profile = request.user.Profile
    profile.logout_time = datetime.datetime.now()
    profile.save()
    auth.logout(request)
    context = {'login': profile.login_time, 'logout': profile.logout_time, 'score': profile.score}
    return render(request, 'Result_page.html', context)


def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(data)
