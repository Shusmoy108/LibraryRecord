from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
import datetime
from local_library.models import Student, Book
from local_library.forms import ContactForm, SearchForm


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


def hours_ahead(request, value):

    dt = datetime.datetime.now() + datetime.timedelta(hours=value)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (value, dt)
    return HttpResponse(html)


def home(request):
    return render(request, 'inherit.html', {})


def templateexample(request):

    return render(request, 'inherit_template.html', {'title': "Django_MySQL_Boiler_Plate", "body": "inherit template page"})


def dash(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            s = Student(roll=form.data['roll'], sclass=form.data['sclass'],
                        fname=form.data['fname'], lname=form.data['lname'])
            s.save()
            print(form.data['roll'])
            return HttpResponseRedirect('/students/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm()

    return render(request, 'inherit.html', {"name": "Managefines", 'formset': ContactForm})


def students(request):
    #students = Student.objects.filter(roll='12')
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SearchForm(request.POST)
        # check whether it's valid:

        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            students = Student.objects.filter(roll=form.data['search'])
        else:
            students = Student.objects.all()

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SearchForm()
        students = Student.objects.all()
    return render(request, 'students.html', {"name": "StudentsList", 'student': students, "form": form})


def book(request):
    books = Book.objects.all()
    print(books)
    return render(request, 'books.html', {"name": "StudentsList", 'books': books})


def index(request):
    students = Student.objects.all()
    print(students)
    return render(request, 'first.html', {"person_name": "Sohel", "company": "Omuk Limited", "item_list": ['chal', 'dal', 'pen', 'pencil'], "ordered_warranty": True})
