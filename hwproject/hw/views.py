from django.shortcuts import render
from django.template import Context, loader
from django.http import HttpResponse
from datetime import datetime


def  index(request):

	return HttpResponse('<html><body>This is the code from "hw" views.py  hw.views.py</body></html>')
	pass
# Create your views here.

def about(request):
		return HttpResponse("This code is in views.py if you click the link you will got to GOOGLE <a href='http://www.google.com'>Back home<a>"
			)

def better(request):
	t=loader.get_template('betterhellow.html')
	c=Context({'current_time': datetime.now(),})
	return HttpResponse(t.render(c))
