import os
from google.cloud import speech_v1p1beta1 as speech
import soundfile as sf

#accessing the json key file
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "D:\Speech-To-Text\google-key.json"

#creating a speech-to-text client object
client = speech.SpeechClient()

#passing the audio for translation
file_path = "D:/Speech-To-Text/test-data/SM1_F1_A01.wav"

data, sample_rate = sf.read(file_path)
print(f'Sample rate: {sample_rate} Hz')

with open(file_path, 'rb') as audio_file:
    content = audio_file.read()

audio = speech.RecognitionAudio(content=content)
config = speech.RecognitionConfig(
    encoding= speech.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=44100,
    language_code='ur-PK',
)

response = client.recognize(config=config, audio=audio)

for result in response.results:
    print(result.alternatives[0].transcript)