from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.http import JsonResponse
from .models import Posesion, Ingreso, Peticion, Codigo
from .forms import CodigoForm
import datetime
from random import randint

# Create your views here.

def getPorCodigo(request):
	repetidas = []
	todas = []
	message=""
	template = loader.get_template('personal.html')
	tempform = CodigoForm(request.POST)
	tempform.is_valid()
	codigo = tempform.cleaned_data['codigo']
	username = request.user.username
	query = Posesion.objects.filter(username=username)
	for p in query:
		if p.contador>1:
			repetidas.append(p.nameFigurita)
	for i in range(1,34):
		for j in range(1, 13):
			todas.append(str(i) + '-' + str(j))
	figuritas = []
	isNewDay = False
	temp=""
	isCodigoValid = False
	result = Codigo.objects.filter(codigo=codigo, isUsed=False)
	if result.count() > 0:
		isCodigoValid = True
		for r in result:
			r.isUsed=True
			r.save()
		for i in range(0,5):
			temp = str(randint(1,33))+"-"+str(randint(1,12))
			figuritas.append(temp)
			p = Posesion()
			p.username = username
			p.nameFigurita = temp
			p.save()
	else:
		message="Código Inválido"
	context = {
		'isNewDay': isNewDay,
		'figuritas': figuritas,
		'isCodigoValid': isCodigoValid,
		'message': message,
		'form':tempform,
		'repetidas':repetidas,
		'todas':todas
		}
	return HttpResponse(template.render(context,request))


def home(request):
	todas = []
	repetidas = []
	message=""
	form = CodigoForm()
	template = loader.get_template('personal.html')
	username = request.user.username
	query = Posesion.objects.filter(username=username)
	for p in query:
		todas.append(p.nameFigurita)
		if p.contador>1:
			repetidas.append(p.nameFigurita)
	figuritas=[]
	isCodigoValid = False
	isNewDay = True
	todays = datetime.date.today()
	result = Ingreso.objects.filter(username=username, monthDay=todays.day, month=todays.month)
	temp=""
	if result.count() == 0:
		isNewDay=True
		newIngreso = Ingreso()
		newIngreso.username = username
		newIngreso.monthDay = todays.day
		newIngreso.month = todays.month
		newIngreso.save()
		country =-1
		player = -1
		for i in range(0,5):
			temp = str(randint(1,33))+"-"+str(randint(1,12))
			figuritas.append(temp)
			p = Posesion()
			p.username = username
			p.nameFigurita = temp
			p.save()
	else:
		isNewDay = False

	context = {
	'isNewDay': isNewDay,
	'figuritas': figuritas,
	'isCodigoValid': isCodigoValid,
	'message':message,
	'form':form,
	'repetidas':repetidas,
	'todas':todas
	}
	return HttpResponse(template.render(context,request))

def peticionIntercambio(request):
    data = {}

    return JsonResponse(data)

def album(request):
	template = loader.get_template('album-virtual.html')
	p = Posesion.objects.filter(username=request.user.username);
	figuritas=[]
	for pos in p:
		figuritas.append(pos.nameFigurita)
	context = {'figuritas':figuritas}
	return HttpResponse(template.render(context,request))
