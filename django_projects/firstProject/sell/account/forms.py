from django import forms
from .forms import Profile

class LoginForm(forms.Form):
    email = forms.EmailField(label = "Email")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

    
    
