from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignupForm(UserCreationForm):
    email = forms.EmailField(label="" ,widget=forms.TextInput(attrs={'class': 'form-control ', 'placeholder': 'Enter your Email'}))
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
    # then do extra stuff:
        # self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'User Name'})
        # self.fields['username'].widget = forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter User Name'})
        # self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'User Name'})
        # self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'User Name'})
        # self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'User Name'})
        self.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter User Name'})
        self.fields['email'].widget= forms.EmailInput(attrs={'class': 'form-control','placeholder': 'Enter Your Mail'})
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'Enter Your Password'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'Confirm Your Password'})