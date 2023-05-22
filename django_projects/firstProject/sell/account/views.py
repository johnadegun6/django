from django.shortcuts import render
from django.http import HttpResponse
from .forms import LoginForm
from django.contrib.auth import login, authenticate
from django.core.exceptions import ValidationError
# # from.forms import Loginform

# from django.core import validators
# from .models import Profile
# from django.core.exceptions import ImproperlyConfigured, ValidationError
# from django.contrib.auth import authenticate, login
# from core.models import Store 

# # Create your views here.

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        try:

            if form.is_valid():
                email=form.cleaned_data['email']
                password=form.cleaned_data['password']
                user = authenticate(email = email, password = password)
                print("User", user.first_name)
                if user is not None:
                    request.session['user_id'] = str(user.id)
                    # login(request, user)
                    print("id", str(user.id), user.first_name, user.last_name)
                return HttpResponse(f"Welcome{user.firstname}")
                # raise ValidationError('Email or Password not correct')
                print("Credentials", email, password)

        except ValidationError as err:
            return render(request,'account/login.html', {'form':form, 'error':err})
            # user = authenticate()

    form = LoginForm()
    return render(request,'account/login.html', {'form':form})

def signup(request): 
    return HttpResponse('User Signed in')

def dashboard(request):
    return HttpResponse('This is your dashboard, welcome')
