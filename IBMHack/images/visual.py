import json
from os.path import join, dirname
from os import environ
from watson_developer_cloud import VisualRecognitionV3

test_url = ''

visual_recognition = VisualRecognitionV3('2016-05-20', api_key='df80546649eaa1d9a9411bcef7a5649e3a453558')



with open('', 'rb') as image_file:
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


print(s);







