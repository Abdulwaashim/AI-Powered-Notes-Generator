import speech_recognition as sr 
import moviepy.editor as mp
import os
name="2.mp4"
pat=os.path.join(r"F:\Projects\AI-Powered-Notes-Generator",name)
clip = mp.VideoFileClip(pat)
clip.audio.write_audiofile(r"converted.wav")
r = sr.Recognizer()
audio = sr.AudioFile("converted.wav")
with audio as source:
    audio_file = r.record(source)
    result = r.recognize_google(audio_file)
    with open('recognized.txt',mode ='w') as file: 
        file.write("Recognized Speech:") 
        file.write("\n") 
        file.write(result) 
        print("ready!")
