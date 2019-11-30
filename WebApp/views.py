from django.shortcuts import render
from django.http import HttpResponseRedirect

from WebApp import forms

def EmpView(request):
    if request.method == 'POST':
        form = forms.EmpForm(request.POST)
        if form.is_valid():
            print("Validations are Success...!!")
            print(form.cleaned_data['Name'])
            print(form.cleaned_data['Salary'])
            print(form.cleaned_data['Opinion'])
            return HttpResponseRedirect('/Thanks')
    else:
        form = forms.EmpForm()
    return render(request, 'WebApp/Form.html', {'form': form})

def ThankView(request):
    return render(request, 'WebApp/Thanks.html')