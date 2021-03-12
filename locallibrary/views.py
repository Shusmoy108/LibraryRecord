from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
import datetime


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
    return render(request, 'inherit.html', {"name": "Managefines"})


def index(request):
    return render(request, 'first.html', {"person_name": "Sohel", "company": "Omuk Limited", "item_list": ['chal', 'dal', 'pen', 'pencil'], "ordered_warranty": True})
