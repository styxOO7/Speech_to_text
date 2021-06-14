import speech_recognition as sr

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening...')
        r.pause_threshold = 2
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        
    try :
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        
        with open("file.txt", 'a') as f:
            # f.next()
            f.write(f"{query}\n")
    
        print(f"The data is successfully written =\n{query}\n")
    except Exception as X:
        print("Say that again...")
    
    return query


if __name__ == '__main__':
    takeCommand()
