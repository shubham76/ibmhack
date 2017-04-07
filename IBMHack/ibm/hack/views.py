from django.http import HttpResponse
from django.shortcuts import render,render_to_response
from django.core.context_processors import csrf 
from .models import person
# Create your views here.

def index(request):
	c={}
	c.update(csrf(request))
	
	return render_to_response('index.html', c)


def  signup(request):
	name=request.POST.get('name','')
	age=(request.POST.get('age',''))
	weight=(request.POST.get('weight',''))
	height=(request.POST.get('height',''))
	password=request.POST.get('pass','')
	gender=request.POST.get('gender','')
	activity=request.POST.get('activity','')

	print(name)
	print(age)
	print(weight)
	print(height)
	print(password)
	print(gender)
	print(activity)

	physicMen = {1:1.0,2:1.12,3:1.27,4:1.54}
	physicWom = {1:1.0,2:1.14,3:1.27,4:1.45}
	
	if(gender=="male"):
		PA = physicMen[int(activity)]
		print PA
		TEE=864-9.72*float(age)+PA*(14.2*float(weight)+503*float(height))
		print(TEE)
	elif(gender=="female"):
		PA = physicWom[int(activity)]
		TEE=387-7.31*float(age)+PA*(10.9*float(weight)+660.7*float(height))
		print(TEE)
	else:
		print("somethings is wrong.")

	obj = person(name=name,age=int(age),weight=float(weight), height=float(height),password=password,gender=gender,activity=activity, tee=TEE)
	obj.save()
	c={}
	c.update(csrf(request))
	
	return render_to_response('login.html', c)


def login(request):
	name=request.POST.get('name','')
	password=request.POST.get('password','')

	user = person.objects.filter(name=name, password=password)
	if len(user)==0:
		c = {'msg':'ID or password incorrect'}
		c.update((csrf(request)))
		return render_to_response('index.html',c)
	user = person.objects.filter(name=name, password=password).first()



	
	c={}
	c.update((csrf(request)))
	return render_to_response('login.html',c)