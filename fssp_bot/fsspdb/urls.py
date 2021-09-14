from django.conf.urls import url,include
from django.urls import  path,re_path
from . import views
# from fsspbotdb.views import  *
urlpatterns = [
    path("", views.index, name='index'),
    path('webhook_status", views.webhook_status, name='webhook_status'),
    #path("HOOK-SyBPwfCLPl30", views.webhook, name='webhook'),
    #path("<slug:slug>", views.webhook, name='webhook'),
    #123


]
