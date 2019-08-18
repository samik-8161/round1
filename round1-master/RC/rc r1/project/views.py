from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.urls import reverse
from .models import Questions, Profile
import re, random

regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
counter = 0


def index1(request):
    if request.method == "POST":
        if request.POST['pass'] == request.POST['passwordagain']:
            try:
                user = User.objects.get(username=request.POST['uname'])
                return render(request, 'signup.html', {'error': "Username Has Already Been Taken"})
            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST['uname'], password=request.POST['pass'])
                p1_name = request.POST['p1_name']
                p2_name = request.POST['p2_name']
                p1_email = request.POST['p1_email']
                p2_email = request.POST['p2_email']
                mob1 = request.POST['mob1']
                mob2 = request.POST['mob2']

                userprofile = Profile(p1_name=p1_name, p2_name=p2_name, p1_email=p1_email, p2_email=p2_email, mob1=mob1,
                                      mob2=mob2, user=user)

            if re.search(regex, p1_email and p2_email):
                userprofile.save()
                auth.login(request, user)
                return redirect(reverse('index2'))
            else:
                return render(request, 'signup.html', {'error': "Email not valid"})
        else:
            return render(request, 'signup.html', {'error': "Passwords Don't Match"})
    else:
        return render(request, 'signup.html')


def index2(request):
    global counter
    qno = random.randint(1, 5)
    questions = Questions.objects.get(pk=qno)
    print(counter)
    context = {'question': questions, 'score': counter}
    return render(request, 'Question.html', context)


def index3(request, qno):
    global counter
    answer = Questions.objects.get(pk=qno)
    ans = request.POST.get('attempt1')
    print(ans)
    print(answer.answer)
    if ans == answer.answer:
        counter = counter + 4
    else:
        ans = request.POST.get('attempt2')
        if ans == answer.answer:
            counter = counter + 2
        else:
            counter = counter - 1
    return redirect(reverse('index2'))
