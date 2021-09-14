from django.shortcuts import render


from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context, Template
from .models import *
import datetime

# Create your views here.

def index (request):

    # p = Food.objects.all()
    # now = datetime.datetime.now()
    # t = get_template('index.html')
    # html = t.render(context={'food':p}, request=None)
    html="OK"
    return HttpResponse(html)
