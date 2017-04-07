import json
from os.path import join, dirname
from watson_developer_cloud import SpeechToTextV1

speech_to_text = SpeechToTextV1(
    username='957c5213-3a11-45a8-8a54-48f08bf29771',
    password='8HXJTa6xvcEi',
    x_watson_learning_opt_out=False
)

#print(json.dumps(speech_to_text.models(), indent=2))

#print(json.dumps(speech_to_text.get_model('en-US_BroadbandModel'), indent=2))

audio_file= open('/home/shubham/Desktop/IBMHack/temp.wav','rb')

str=json.dumps(speech_to_text.recognize(audio_file, content_type='audio/wav', timestamps=True,word_confidence=True),indent=2)

dict=json.loads(str)
s=""
try:
	s=(dict['results'][0]['alternatives'][0]["transcript"])
except:
	s=("Colud not recognise the voice :(. Please try again.")
  

print s





'''

with open( '/home/shubham/Desktop/temp.wav',
          'rb') as audio_file:
    print(json.dumps(speech_to_text.recognize(
        audio_file, content_type='audio/wav', timestamps=False,
        word_confidence=False),
        indent=2))
'''