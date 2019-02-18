from django import forms

class Login_Form(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput())
    