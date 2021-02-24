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


def index(request):
    return render(request, 'index.html', {})
