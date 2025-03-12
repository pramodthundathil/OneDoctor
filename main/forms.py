from django.forms import fields, forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import DoctorAdd


class UserRegistration(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']

    
        widgets = {
                "username":forms.TextInput(attrs={"class":"form-control", "placeholder":"Username"}),
                "first_name":forms.TextInput(attrs={"class":"form-control","placeholder":"First Name"}),
                "last_name":forms.TextInput(attrs={"class":"form-control","placeholder":"last name"}),
                "email":forms.EmailInput(attrs={"class":"form-control","placeholder":"Email"}),
               
            
            }

    def __init__(self, *args, **kwargs):
        super(UserRegistration, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control  py-3', 'placeholder': 'Password'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control  py-3', 'placeholder': 'Password confirmation'})



class DoctorAddForm(forms.ModelForm):
    class Meta:
        model = DoctorAdd
        fields = ['Doctor_name', 'Doctor_spacial', 'Date_joined']
        widgets = {
            'Doctor_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Doctor Name'}),
            'Doctor_spacial': forms.Select(attrs={'class': 'form-control'}),
            'Date_joined': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Date Joined', 'type': 'date'}),
        }