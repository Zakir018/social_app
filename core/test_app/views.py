from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate,logout

# Create your views here.
def index(request):
    return render(request, 'test_app/index.html')

def signup(request):
    message = ""
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        repeat_password = request.POST.get('repeat_password')
        if password != repeat_password:
            message = "your password not mactch"

        elif len(password) < 8:
            message = "your password is too short"

        elif User.objects.filter(username=username).exists():
            message = "username alread token"

        elif User.objects.filter(email=email).exists():
            message = "email alread token"

        user = User.objects.create_user(
            username=username.lower(),
            password=password
        )
        # user.save()
        
    
    return render(request, 'test_app/signup.html',{"message":message})

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("login_username")
        password = request.POST.get("login_password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
    return render(request, 'test_app/login.html')

