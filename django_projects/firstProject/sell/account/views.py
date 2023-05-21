from django.shortcuts import render
from django.http import HttpResponse
# from.forms import Loginform
# Create your views here.

def login(request):
    return HttpResponse('User logged in')

def signup(request):
    return HttpResponse('User Signed in')

def dashboard(request):
    return HttpResponse('This is your dashboard, welcome')
