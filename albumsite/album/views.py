from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse,Http404,HttpResponseRedirect

# Create your views here.

def home(request):
	template = loader.get_template('personal.html')
	context = {}
	return HttpResponse(template.render(context,request))
