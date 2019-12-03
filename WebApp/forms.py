from django import forms
from django.core import validators
# from django.core.validators import validate_email
# from django.core.exceptions import ValidationError

def Begin_With( value ):
    if value[0] != 'S':
        raise forms.ValidationError("Sorry Name Must Starts With S")

# def Begin_With_Alpha( value ):
#     if value.isalpha() != True:
#         raise forms.ValidationError("SorryNameMustBeStartsWithAlphabets")

# def ValidateEmail( email ):
#     ValidationError
    

class EmpForm(forms.Form):
    Name = forms.CharField(validators = [Begin_With])
    # Email = forms.CharField(validators = validators.EmailValidator())
    Salary = forms.IntegerField()
    # Opinion = forms.CharField(validators = [Begin_With_Alpha])
    # Opinion = forms.CharField(
    #     widget = forms.Textarea, 
    #     validators = [validators.MaxLengthValidator(50), 
    #     validators.MinLengthValidator(10), 
    #     Begin_With_Alpha,
    #     validators.RegexValidator(regex='[a-zA-Z0-9]*$', message='UserName must be alphanumeric', code='Invalid_Username')
    #     ],
    Bot_Field = forms.CharField(required= False, widget= forms.HiddenInput)
    

    def clean(self):
        cdata = super().clean()
        bhandel = cdata['Bot_Field']
        if len(bhandel) > 0:
            raise forms.ValidationError('Welcome You BOT, Your Data unable to process')

def clean(self):
    super().clean()