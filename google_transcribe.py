import os
from google.cloud import speech_v1p1beta1 as speech
import soundfile as sf
from memory_profiler import profile
from line_profiler import LineProfiler
from test_accuracy import check_similarity

file_path = "D:/Speech-To-Text/test-data/verysmall.wav"

# @profile(precision= 4)

def transcribe(file_path):
#accessing the json key file
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "D:\Speech-To-Text\google-key.json"

    #creating a speech-to-text client object
    client = speech.SpeechClient()

    data, sample_rate = sf.read(file_path)
    # print(f'Sample rate: {sample_rate} Hz')

    first_lang = 'ur-PK'
    second_lang = 'en-UK'

    with open(file_path, 'rb') as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding= speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=sample_rate,
        language_code= first_lang,
    )

    response = client.recognize(config=config, audio=audio)

    for result in response.results:
        # print(result.alternatives[0].transcript)
        return result.alternatives[0].transcript
        
        
STT = transcribe(file_path)
# print(STT)
# path = file_path
# lp = LineProfiler()
# lp_wrapper = lp(transcribe.__wrapped__)
# lp_wrapper(path)
# lp.print_stats()

# print("آپ کیسے ہو")

with open('./results/vsmall_result.txt', 'w', encoding='utf-8') as f:
    f.write(STT)
 
check_similarity("very small", STT)