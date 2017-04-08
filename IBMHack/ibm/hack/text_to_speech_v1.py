# coding=utf-8
import json
import pyaudio
import wave
from os.path import join, dirname
from watson_developer_cloud import TextToSpeechV1

def change(str):
	text_to_speech = TextToSpeechV1(
       username='2a352fa9-fdfc-47b9-83b5-3f4ac61c8226',
       password='wjazlNHVRioz',
       x_watson_learning_opt_out=True
       )  # Optional flag

	with open('/home/shubham/Desktop/temp.wav','wb') as audio_file:
		audio_file.write(text_to_speech.synthesize(str, accept='audio/wav',voice="en-US_AllisonVoice"))
  
	chunk = 1024  

	#open a wav format music  
	f = wave.open(r"/home/shubham/Desktop/temp.wav","rb")  
	#instantiate PyAudio  
	p = pyaudio.PyAudio()  
	#open stream  
	stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
	                channels = f.getnchannels(),  
	                rate = f.getframerate(),  
	                output = True)  
	#read data  
	data = f.readframes(chunk)  

	#play stream  
	while data:  
	    stream.write(data)  
	    data = f.readframes(chunk)  

	#stop stream  
	stream.stop_stream()  
	stream.close()  

	#close PyAudio  
	p.terminate()




	# print(json.dumps(text_to_speech.create_customization('test-customization'),
	#  indent=2))

	# print(text_to_speech.update_customization('YOUR CUSTOMIZATION ID',
	# name='new name'))

	# print(json.dumps(text_to_speech.get_customization('YOUR CUSTOMIZATION ID'),
	#  indent=2))

	# print(json.dumps(text_to_speech.get_customization_words('YOUR CUSTOMIZATION
	#  ID'), indent=2))

	# print(text_to_speech.add_customization_words('YOUR CUSTOMIZATION ID',
	#                                              [{'word': 'resume',
	# 'translation': 'rɛzʊmeɪ'}]))

	# print(text_to_speech.set_customization_word('YOUR CUSTOMIZATION ID',
	# word='resume',
	#                                             translation='rɛzʊmeɪ'))

	# print(json.dumps(text_to_speech.get_customization_word('YOUR CUSTOMIZATION
	# ID', 'resume'), indent=2))

	# print(text_to_speech.delete_customization_word('YOUR CUSTOMIZATION ID',
	# 'resume'))

	# print(text_to_speech.delete_customization('YOUR CUSTOMIZATION ID'))
