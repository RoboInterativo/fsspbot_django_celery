from django.shortcuts import render


from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context, Template
from .models import *
import datetime
import requests
import yaml

# Create your views here.
with open('/home/django/config.yml') as f:
    config=yaml.safe_load(f)

TELEGRAM_TOKEN= config.get('TELEGRAM_TOKEN')


def webhook_status(request):
    method='getWebhookInfo'
    url=f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/{method}'
    r=requests.get(url)
    return HttpResponse(r.text())

def index (request):

    # p = Food.objects.all()
    # now = datetime.datetime.now()
    # t = get_template('index.html')
    # html = t.render(context={'food':p}, request=None)
    html="OK"
    return HttpResponse(html)
