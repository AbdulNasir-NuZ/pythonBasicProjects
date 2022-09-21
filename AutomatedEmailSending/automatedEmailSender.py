import speech_recognition as sr
import yagmail 

recognizer = sr.Recognizer()
with sr.Microphone() as source:
    print('Noise reduction')
    recognizer.adjust_for_ambient_noise(source, duration=1)
    print('waiting for your message..')
    recordedaudio = recognizer.listen(source)
    print('Done Recording..!')
    try :
        print('Printing the message.....')
        text = recognizer.recognize_google(recordedaudio, language='en-US')
    
        print('Your message:{}'.format(text))
       
    except Exception as ex:
         print(ex)

# Mail Automation:
reciever = 'coderfile06@gmail.com'
msg = text 
sender = yagmail.SMTP('nasir.nuz@gmail.com')
sender.send(to=reciever,subject ='This is an automated Mail', contents=msg)