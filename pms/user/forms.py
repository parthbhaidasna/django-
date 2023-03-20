from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import User

class ManagerRegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Re-enter Password'}),
        }

        forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_manager = True
        user.save()
        return user
    
class DeveloperRegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Re-enter Password'}),
        }
        

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_developer = True
        user.save()
        return user
    
class TeamLeaderRegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Re-enter Password'}),
        }
        

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_teamleader = True
        user.save()
        return user
    
class TesterRegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Re-enter Password'}),
        }
        

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_tester = True
        user.save()
        return user