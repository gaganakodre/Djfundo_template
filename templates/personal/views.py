from urllib import response

from django.contrib.auth import authenticate, login
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import redirect, render
# importing loading from django template
from django.template import loader

from . models import User


def index(request):
    template = loader.get_template('index.html')  # getting our template
    name = {
        'student': 'rahul'
    }
    return HttpResponse(template.render(name))  # rendering the template in HttpResponse


def register(request):
    # template = loader.get_template('register.html') # getting our template

    if request.method == "POST":

        email = request.POST["email"]
        username = request.POST["username"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        password = request.POST["password"]
        # if email == "" or username == "" or password == "":
        #     return redirect('user/register')
        User.objects.create_user(email=email, username=username, first_name=first_name, last_name=last_name,
                                 password=password)
        return redirect('login')

    return render(request, 'user/register.html')


def login_view(request):
    try:
        if request.method == "POST":
            email = request.POST["email"]
            password = request.POST["password"]
            user = authenticate(email=request.POST["email"], password=request.POST["password"])
            if user:
                login(request, user)
                return redirect('home')
        return render(request, 'user/login.html')
    except Exception as e:
        print(e)
        return render(request, 'user/login.html')


def home_view(request):
    template = loader.get_template('user/home.html')  # getting our template
    name = {
        'student': 'rahul'
    }
    return render(request, 'user/home.html')
