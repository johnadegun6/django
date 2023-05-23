from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LoginForm
from django.contrib.auth import login, authenticate
from django.core.exceptions import ValidationError
from .models import Profile
from sell.models import Store
from .forms import SignUpForm

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
                # print("User", user.first_name)
                if user is not None:
                    request.session['user_id'] = str(user.id)
                    return redirect('dashboard')
                #     # login(request, user)
                #     print("id", str(user.id), user.first_name, user.last_name)
                # return HttpResponse(f"Welcome{user.firstname}")
                # # raise ValidationError('Email or Password not correct')
                # print("Credentials", email, password)

        except ValidationError as err:
            return render(request,'account/login.html', {'form':form, 'error':err})
            # user = authenticate()

    form = LoginForm()
    return render(request,'account/login.html', {'form':form})

def signup(request): 
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            address = form.cleaned_data['address']
            phone_number = form.cleaned_data['phone_number']
            user = Profile(username=username, email=email, first_name=first_name, last_name=last_name, address=address, phone_number=phone_number)
            form.save()
            return redirect('login')
    form = SignUpForm()
    # return HttpResponse('User Signed in')
    return render(request, 'account/signup.html',{'form':form})

def dashboard(request):
    user_id = request.session['user_id']
    user = Profile.objects.get(id=user_id)
    # return HttpResponse('This is your dashboard, welcome')
    store=Store.objects.get(owner=user)
    return render(request, 'account/dashboard.html', {'store':store})