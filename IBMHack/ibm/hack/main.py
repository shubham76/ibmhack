import operator
import collections
from collections import OrderedDict
from operator import itemgetter
"""
fname = raw_input("Your name here:")
weight = int(raw_input("Put your weight here in kg: "))
height = float(raw_input("Put your height here in meters: "))
age = int(raw_input("Your age here: "))
gender = int(raw_input("What's your gender?\n1.male\n2.female?\n")) 
activity = int(raw_input("Choose one of the following activity of yours : \n1.Sedentary\n2.Low Active\n3.Active\n4.Very Active\n"))


physicMen = {1:1.0,2:1.12,3:1.27,4:1.54}
physicWom = {1:1.0,2:1.14,3:1.27,4:1.45}

print(physicWom[activity])

if(gender==1):
	PA = physicMen[activity]
	print PA
	TEE=864-9.72*age+PA*(14.2*weight+503*height)
	print(TEE)
elif(gender==2):
	PA = physicWom[activity]
	TEE=387-7.31*age+PA*(10.9*weight+660.7*height)
	print(TEE)
else:
	print("somethings is wrong.")

"""
def calc(li, TEE):

	ans = ""

	breakfast = {'espresso':9,'pepperoni pizza':800,'chip':500,'french fries':500,'chapatti':100,'scrambled egg':150,'chocolate fudge':300,'chow mein':460,'cheeseburger':400,'white bread':265,'cabbage':25,'cauliflower':30,'coriander':45,'curry':110,'drumstick':25,'fenugreek':20,'lettuce':20,'mint':50,'raddish':30,'spinach':25,'ash gourd':10,'bitter gourd':25,'bottle gourd':10,'brinjal':25,'broad beans':50,'cluster beans':15,'drumstick':25,'french bean':25,'green peas':95,'jackfruit':135,'ladies finger':35,'mango':45,'papaya':30,'pumpkin':25,'capsicum':25,'tomato':20,'channa dal':370,'whole moong':335,'moong dal':350,'masoor dal':345,'peas':315,'rajmah':345,'red gram dal':335,'soya beans':430,'amla':60,'apple':60,'appricot':305,'banana':115,'cherries':65,'chickoo':100,'currants':315,'dates':315,'figs':35,'grapes':70,'guava':50,'lemon':55,'lichee':60,'sweet lime':35,'mango':75,'watermelon':15,'orange':50,'papaya':30,'peach':50,'pineapple':70,'rasperry':55,'strawberry':45,'custard apple':105,'bajra':360,'barley':335,'jowar':350,'maize':340,'rice':350,'riceflakes':345,'rice puffed':325,'wheat flour':340,'rawa':350,'wheat vermicelli':350,'wheat bread':245,'sago':350,'almond':655,'cashewnut':595,'coconut':660,'ground nuts':565,'walnut':690,'sugarcane':400,'honey':320,'jaggery':385,'white sugar':400,'beef':115,'buffalo':85,'duck':130,'egg':175,'chicken':110,'milk':65,'curd':60,'paneer':355,'cheese':350,'desert':300,'pattice':150,'potato poha':150,'samosa':150,'cutlet':150,'alu tikki':100,'dosa':120,'masala dosa':120,'idli':200,'fish fingers':170,'french fries':300,'potato chips':550,'milk chocolate':520,'cheese piza':250}

	food = OrderedDict(sorted(breakfast.items(), key=itemgetter(1)))

	print food

	reward={'biscuit':50,'rosogulla':100,'jalebi':150,'ice-cream':200,'sponge cake':250,'chocolate cake':300,'shrikhand':350,'tacos':400,'potato chips':450,'french fries':500,'donuts':550,'subway sandwich':600,'kfc krisper':650,'burger':700,'ice-cream-shake':750,'pizza':800}

	sum=0

	for item in li:
		sum+=breakfast[item]



	print (TEE)

	if(abs(TEE-sum) <= 50):
		ans+="Good Going. Keep It Up. "
	elif(sum < TEE):
		ans+="You have eaten less than required. "
		s=(TEE)-sum
		print (sum)
		ans+="Reward yourself with one of these: "
		for key, value in reward.iteritems():
			a=value-s
			if(abs(a)<=25):
				ans+=key+" "
			
	else:
		aa = {}

		for item in li:
			aa[item]=food[item]

		ans+="You shouldn't have eaten these items:- "
		newaa=OrderedDict(sorted(aa.items(), key=itemgetter(1),reverse=True))
		val=sum-(TEE)
		sat=0
		for x in newaa:
			if(sat+newaa[x]<=val):
				sat+=newaa[x]
				ans+=x+" "

	return ans


