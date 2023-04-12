import speech_recognition as sr

r = sr.Recognizer()

file_path = 'D:/Speech-To-Text/test-data/SM1_F1_A01.wav'
transcribe_file = sr.AudioFile(file_path)
with transcribe_file as source:
    audio = r.record(source)

print(type(audio))
# output = r.recognize_google(audio, language= 'ur-PK')
output = r.recognize_google(audio)
print(output)

