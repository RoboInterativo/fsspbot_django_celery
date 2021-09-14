from django.shortcuts import render

# Create your views here.

def index (request):

    # p = Food.objects.all()
    # now = datetime.datetime.now()
    # t = get_template('index.html')
    # html = t.render(context={'food':p}, request=None)
    html="OK"
    return HttpResponse(html)
