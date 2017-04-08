from django.http import HttpResponse
from django.shortcuts import render,render_to_response
from django.core.context_processors import csrf 
from .models import person, images
from .forms import UploadFileForm
import json
from os.path import join, dirname
from os import environ
from watson_developer_cloud import VisualRecognitionV3
import operator
import collections
from collections import OrderedDict
from operator import itemgetter
from main import calc
from text_to_speech_v1 import change
def index(request):
	c={}
	c.update(csrf(request))
	
	return render_to_response('index.html', c)

def visual(path):
	test_url = path

	visual_recognition = VisualRecognitionV3('2016-05-20', api_key='df80546649eaa1d9a9411bcef7a5649e3a453558')



	with open(path, 'rb') as image_file:
	    str=json.dumps(
	        visual_recognition.classify(images_file=image_file, threshold=0.1,
	                                    classifier_ids=['CarsvsTrucks_1479118188',
	                                                    'default']), indent=2)


	dict=json.loads(str)

	s=""

	try:
		#s=(dict['results'][0]['alternatives'][0]["transcript"])
		s=(dict['images'][0]['classifiers'][0]['classes'][0]['class'])

	except:
		s=("Could not recognise the voice :(. Please try again.")


	return s


def  signup(request):
	name=request.POST.get('name','')
	age=(request.POST.get('age',''))
	weight=(request.POST.get('weight',''))
	height=(request.POST.get('height',''))
	password=request.POST.get('pass','')
	gender=request.POST.get('gender','')
	activity=request.POST.get('activity','')
	option=request.POST.get('option','')

	option=int(option)

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

	if(option==1):
		TEE-=500
	elif (option==2):
		TEE+=300
	else:
		print("Asdf")	
	
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

	request.session['name'] = name

	c={}
	c.update((csrf(request)))
	return render_to_response('upload.html',c)


def  upload(request):

	fil = request.FILES['img']
	name = fil.name

	#obj = images(item=name)
	#obj.save()
	path = "hack/static/images1/"+name
	with open(path, 'wb+') as destination:
		for chunk in fil.chunks():
			destination.write(chunk)

	breakfast = {'espresso':9,'pepperoni pizza':800,'chip':500,'french fries':500,'chapatti':100,'scrambled egg':150,'chocolate fudge':300,'chow mein':460,'cheeseburger':400,'white bread':265,'cabbage':25,'cauliflower':30,'coriander':45,'curry':110,'drumstick':25,'fenugreek':20,'lettuce':20,'mint':50,'raddish':30,'spinach':25,'ash gourd':10,'bitter gourd':25,'bottle gourd':10,'brinjal':25,'broad beans':50,'cluster beans':15,'drumstick':25,'french bean':25,'green peas':95,'jackfruit':135,'ladies finger':35,'mango':45,'papaya':30,'pumpkin':25,'capsicum':25,'tomato':20,'channa dal':370,'whole moong':335,'moong dal':350,'masoor dal':345,'peas':315,'rajmah':345,'red gram dal':335,'soya beans':430,'amla':60,'apple':60,'appricot':305,'banana':115,'cherries':65,'chickoo':100,'currants':315,'dates':315,'figs':35,'grapes':70,'guava':50,'lemon':55,'lichee':60,'sweet lime':35,'mango':75,'watermelon':15,'orange':50,'papaya':30,'peach':50,'pineapple':70,'rasperry':55,'strawberry':45,'custard apple':105,'bajra':360,'barley':335,'jowar':350,'maize':340,'rice':350,'riceflakes':345,'rice puffed':325,'wheat flour':340,'rawa':350,'wheat vermicelli':350,'wheat bread':245,'sago':350,'almond':655,'cashewnut':595,'coconut':660,'ground nuts':565,'walnut':690,'sugarcane':400,'honey':320,'jaggery':385,'white sugar':400,'beef':115,'buffalo':85,'duck':130,'egg':175,'chicken':110,'milk':65,'curd':60,'paneer':355,'cheese':350,'desert':300,'pattice':150,'potato poha':150,'samosa':150,'cutlet':150,'alu tikki':100,'dosa':120,'masala dosa':120,'idli':200,'fish fingers':170,'french fries':300,'potato chips':550,'milk chocolate':520,'cheese piza':250}

	food = OrderedDict(sorted(breakfast.items(), key=itemgetter(1)))

	item_name=visual(path)
	calorie=food[item_name]

	user_name=request.session.get('name','')
	
	obj = images(image_name=name,item_name=item_name,calorie=calorie,name=user_name)
	obj.save()

	c={}
	c.update((csrf(request)))
	return render_to_response('upload.html',c)


def calculate(request):
	name=request.session.get('name','')
	user = images.objects.filter(name=name)	

	li = []
	total_colorie = 0
	for t in user:
		total_colorie+=t.calorie
		li.append(t.item_name)

	usertee = person.objects.filter(name=name)
	for t in usertee:
		TEE=t.tee

	ans=calc(li,TEE)
	print li
	print total_colorie
	change(ans)
	c = {'msg':ans}
	c.update((csrf(request)))
	return render_to_response('upload.html',c)
