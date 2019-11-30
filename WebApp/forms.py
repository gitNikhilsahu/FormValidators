from django import forms
from django.core import validators

class EmpForm(forms.Form):
    Name = forms.CharField()
    Salary = forms.IntegerField()
    Opinion = forms.CharField(widget=forms.Textarea, validators=[validators.MaxLengthValidator(50), validators.MinLengthValidator(10)])