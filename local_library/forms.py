from django.forms import ModelForm
from local_library.models import Student
from django import forms


class ContactForm(ModelForm):
    class Meta:
        model = Student
        fields = ['roll', 'sclass', 'fname', 'lname']


class SearchForm(forms.Form):
    search = forms.CharField(max_length=100)
