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

#TELEGRAM_TOKEN= config.get('TELEGRAM_TOKEN')

def set_webhook(request):
    TELEGRAM_TOKEN=request.get('token')
    method='setWebhook'
    url=f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/{method}'
    tel_url="https://174.138.1.184/webhook"
    r=requests.get(url,{'url':tel_url})
    return HttpResponse(r.text )

def delete_webhook(request):
    TELEGRAM_TOKEN=request.get('token')
    method='deleteWebhook'
    url=f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/{method}'
    r=requests.get(url)
    return HttpResponse(r.text )

def webhook_status(request):
    TELEGRAM_TOKEN=request.get('token')
    method='getWebhookInfo'
    url=f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/{method}'
    r=requests.get(url)
    return HttpResponse(r.text )

def index (request):

    # p = Food.objects.all()
    # now = datetime.datetime.now()
    # t = get_template('index.html')
    # html = t.render(context={'food':p}, request=None)
    html="OK"
    return HttpResponse(html)
