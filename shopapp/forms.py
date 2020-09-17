from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

#Creating a register form
class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        # getting username,email,password,confirmpassword
        fields =['username','email','password1','password2']

# creating form for login
class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

gender_choice = [
    ('male','Male'),
    ('female','Female')
]

class ProfileForm(forms.ModelForm):
    gender = forms.CharField(widget=forms.RadioSelect(choices=gender_choice))
    class Meta:
        model = Profile
        fields = ['user_image','first_name','last_name','gender','address','phone_number']