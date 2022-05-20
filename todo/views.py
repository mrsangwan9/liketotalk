from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from .models import MyUser


def terms(request):
    return HttpResponse("That's your space and their is no terms and condition..live your life freely")


def signupp(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        hash_pwd = make_password(password)
        alluser = MyUser.objects.all()
        for users in alluser:
            if users.email == email:
                return render(request, "signup.html", {"error": "your email already register try differenet or login.", })
            else:
                continue
    #     fm = User.objects.create_user(username, pass1, pass2)
            #     fm.save()
        Users = MyUser(name=fname, lastname=lname,
                       email=email, password=hash_pwd)
        Users.save()
        return HttpResponse("account created ")
    else:
        return render(request, "signup.html")


def loginn(request):
    if request.method == "POST":
        email = request.POST.get('email')
        pass1 = request.POST.get('password')
        user = authenticate(username=email, password=pass1)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/profile')
        else:
            return render(request, "login.html", {"error": "invalid email or password"})
    else:
        return render(request, "login.html")


def profile(request):
    if request.user.is_authenticated:
        alluser = MyUser.objects.all()
        return render(request, "profile.html", {"username": request.user.name,"users":alluser})
    else:
        return HttpResponseRedirect("/login")






def messagee(request, other_user_id):
    if request.user.is_authenticated:
           sendby=request.user.name
           other_user = MyUser.objects.get(id=other_user_id)
           return render(request,"message.html",{"other_user_id":other_user_id,"sender":sendby,"other_user":other_user})
    else:
        return HttpResponseRedirect("/login")  

def logoutt(request):
    logout(request)
    return HttpResponseRedirect("/login")
