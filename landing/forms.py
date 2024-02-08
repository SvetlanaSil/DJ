from django import forms

class MyForm(forms.Form):
    Name = forms.CharField()
    Email = forms.EmailField()
    Subject = forms.CharField()
    Message = forms.CharField()