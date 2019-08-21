import datetime
import random
import re

from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login, logout

from .models import Questions, Profile, Score, LILO

regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
counter = 0
temp1 = ''
temp2 = ''
x = 1


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
                userprofile.save()
                auth.login(request, user)
                LILO.login_time=datetime.datetime.now(login(request,user))
                return redirect(reverse('index2'))
            else:
                return render(request, 'signup.html', {'error': "Email not valid"})
        else:
            return render(request, 'signup.html', {'error': "Passwords Don't Match"})
    else:
        return render(request, 'signup.html')


def index2(request):
    global counter
    qno = random.randint(1, 4)
    questions = Questions.objects.get(pk=qno)
    print(counter)
    context = {'question': questions, 'score': counter}
    return render(request, 'Question.html', context)


def index3(request, qno):
    global counter, temp1, temp2, x
    answer = Questions.objects.get(pk=qno)
    ans = request.POST.get('options')
    a = Score.objects.get(pk=1).count
    b = Score.objects.get(pk=2).count
    c = Score.objects.get(pk=3).count
    d = Score.objects.get(pk=4).count
    print(answer.answer)
    print(ans)
    for i in range(x, 4):

        if answer.answer == ans and i == 1:
            counter = counter + a
            x = 2
        elif answer.answer != ans and i == 1:
            counter = counter - b
            x = 2

        elif answer.answer == ans and temp1 == temp2:
            counter = counter + a
        elif answer.answer != ans and temp1 == temp2:
            counter = counter - b
        elif answer.answer == ans and temp1 != temp2:
            counter = counter + c
        else:
            counter = counter - d
        break

    temp1 = answer.answer
    temp2 = ans
    print(counter)
    return redirect(reverse('index2'))


def login_logout(request):
    if request.POST.get=='logout':
        auth.logout(request,Profile.user)
        LILO.logout_time = datetime.datetime.now()
    context = {'login': LILO.login_time, 'logout': LILO.logout_time, 'score': counter}
    return render(request, 'Result_page.html', context)




