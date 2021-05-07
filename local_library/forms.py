from django.forms import ModelForm
from local_library.models import Student


class ContactForm(ModelForm):
    class Meta:
        model = Student
        fields = ['roll', 'sclass', 'fname', 'lname']
