from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm  
from .forms import SignupForm
from .models import *
# Create your views here.
def loginPage(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password = password)
        if user is not None:
            login(request, user)
            return redirect("Freelancing:home")
            print("Login")
        else:
            # messages.warning(request, "Username or Password is incorrect")
            return redirect("Freelancing:login")
            print("Error")

    else:
        return render (request, 'login.html', {})


def logoutPage(request):
    logout(request)
    return redirect("Freelancing:login")

def registerPage(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password1 =  form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            # messages.success(request, "Account was created for "+user)
            return redirect('FoodApp:loginPage')
    context={'form':form}
   
    return render( request, 'register.html', context)

def home(request):
    return render(request, 'index.html', {})

