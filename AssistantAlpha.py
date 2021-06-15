from tkinter import *
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import operator

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 190)

window = Tk()

global var
global var1

var = StringVar()
var1 = StringVar()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        var.set("Good Morning !")
        window.update()
        speak("Good Morning !")
    elif hour >= 12 and hour <= 18:
        var.set("Good Afternoon !")
        window.update()
        speak("Good Afternoon !")
    else:
        var.set("Good Evening ! ")
        window.update()
        speak("Good Evening !")
    speak("Hello,I am Alpha! How may I help you?")

def sendemail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('emailid', 'password') #enter your email id and password
    server.sendmail('emailid', to, content)
    server.close()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        var.set("Listening...")
        window.update()
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 400
        audio = r.listen(source,timeout=0.5,phrase_time_limit=4)
    try:
        var.set("Recognizing...")
        window.update()
        print("Recognizing")
        query = r.recognize_google(audio, language='en-in')
    except Exception as e:
        return "None"
    var1.set(query)
    window.update()
    return query


def play():
    btn2['state'] = 'disabled'
    btn0['state'] = 'disabled'
    btn1.configure(bg='orange')
    wishme()
    while True:
        btn1.configure(bg='orange')
        query = takeCommand().lower()
        if 'exit' in query:
            var.set("Bye..Have a good day!")
            btn1.configure(bg='#5C85FB')
            btn2['state'] = 'normal'
            btn0['state'] = 'normal'
            window.update()
            speak("Bye..Have a good day ")
            break

        elif 'wikipedia' in query or 'search' in query:
            if 'open wikipedia' in query:
                webbrowser.open('wikipedia.com')
            else:
                try:
                    speak("searching wikipedia")
                    query = query.replace("According to wikipedia", "")
                    results = wikipedia.summary(query, sentences=1)
                    var.set(results)
                    window.update()
                    speak("According to wikipedia")
                    speak(results)
                except Exception as e:
                    var.set('Sorry could not find any results')
                    window.update()
                    speak('Sorry could not find any results')

        elif 'open youtube' in query or 'youtube' in query:
            var.set('opening Youtube')
            window.update()
            speak('opening Youtube')
            webbrowser.open("youtube.com")

        elif 'open course era' in query or 'coursera' in query or 'course error' in query:
            var.set('opening coursera')
            window.update()
            speak('opening coursera')
            webbrowser.open("coursera.com")

        elif 'open google' in query or 'google' in query:
            var.set('opening google')
            window.update()
            speak('opening google')
            webbrowser.open("google.com")
            

        elif 'open stack overflow' in query or 'stack overflow' in query:
            var.set('opening stackoverflow')
            window.update()
            speak('opening stackoverflow')
            webbrowser.open('stackoverflow.com')

        elif 'play music' in query or 'music' in query:
            music_dir = 'D:\\#Sem 4\\python\\Project\\AssistantAlpha\\music' #enter path ins your device
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
            
        elif 'time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            var.set("The time is %s" % strtime)
            window.update()
            speak("The time is %s" % strtime)

        elif 'date' in query:
            strdate = datetime.datetime.today().strftime("%d %m %y")
            var.set("Sir today's date is %s" % strdate)
            window.update()
            speak("Sir today's date is %s" % strdate)

        elif 'thank you' in query:
            var.set("You're Welcome!")
            window.update()
            speak("You're Welcome!")

        elif 'can you' in query:
            var.set('I can do multiple tasks for you \nlike search on web, send email, calculation. \nTell me what do you want to perform.')
            window.update()
            speak('I can do multiple tasks for you like search on web, send email and perform calculation. Tell me what do you want to perform.')

        elif 'open media player' in query:
            var.set("opening VLC media Player")
            window.update()
            speak("opening V L C media player")
            path = "C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"  #enter path in your device
            os.startfile(path)

        elif 'your name' in query:
            var.set("My name is Alpha")
            window.update()
            speak('My name is Alpha')

        elif 'hello' in query:
            var.set('Hello! I am Alpha .Please tell me how may I help you.')
            window.update()
            speak('Hello! I am Alpha .Please tell me how may I help you.')

        elif 'open pycharm' in query:
            var.set("Opening Pycharm")
            window.update()
            speak("Opening Pycharm")
            path = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.1\\bin\\pycharm64.exe"  #enter path in your device
            os.startfile(path)

        elif 'open chrome' in query:
            var.set("Opening Google Chrome")
            window.update()
            speak("Opening Google Chrome")
            path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"  #enter path in your device
            os.startfile(path)
    
        
        elif "open python" in query:
            var.set("Opening Python IDLE")
            window.update()
            speak('opening python I D L E')
            os.startfile("C:\\Users\\Win10\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.9\\IDLE (Python 3.9 64-bit).lnk") #enter path in your device

        elif 'open notepad' in query:
            var.set('Opening Notepad')
            window.update()
            speak('opening Notepad')
            npath = "C:\\WINDOWS\\system32\\notepad.exe" #enter path in your device
            os.startfile(npath)

        elif 'open command prompt' in query:
            var.set('Opening Command prompt')
            window.update()
            speak('opening Command prompt')
            os.system("start cmd")


        elif 'calculate' in query:
            var.set('Yes , please tell what you want to calculate')
            window.update()
            speak('Yes , please tell what you want to calculate')
            while True:
                try:
                    query = takeCommand()
                except Exception as e:
                    print(e)
                    var.set("Sorry ! Couldn't understand")
                    window.update()
                    speak("Sorry ! Couldn't understand")
                def get_operator_fn(op):
                     return {
                         '+' : operator.add,
                         '-' : operator.sub,
                         'x' : operator.mul,
                         'divided' :operator.__truediv__,
                         'Mod' : operator.mod,
                         'mod' : operator.mod,
                         'power': operator.__pow__,
                         }[op]
                    
                def eval_binary_expr(op1, oper, op2):
                      op1,op2 = int(op1), int(op2)
                      return get_operator_fn(oper)(op1, op2)
                                    
                result=eval_binary_expr(*(query.split()))
                var.set('Result: ' + str(result))
                window.update()
                speak('Here is the result' + str(result))
                try:
                    query = takeCommand()
                except Exception as e:
                    print(e)
                    var.set("Sorry ! Couldn't understand")
                    window.update()
                    speak("Sorry ! Couldn't understand")
                if 'done' in query:
                    break
                else:
                    var.set('What else do you want to calculate?')
                    window.update()
                    speak('What else do you want to calculate?')

        elif 'email' in query:
            try:
                var.set("What should I say")
                window.update()
                speak('what should I say')
                content = takeCommand()
                to = "tanaya.raikwar00@gmail.com"
                sendemail(to, content)
                var.set('Email has been sent!')
                window.update()
                speak('Email has been sent!')

            except Exception as e:
                print(e)
                var.set("Sorry ! I was not able to send this email")
                window.update()
                speak('Sorry ! I was not able to send this email')
                                     

            
       

def update(ind):
    frame = frames[(ind) % 100]
    ind += 1
    if ind > 30:  # With this condition it will play gif infinitely
        ind = 0
    label.configure(image=frame, bg='#06225F',width=900,height=500)
    window.after(100, update, ind)


label2 = Label(window, textvariable=var1, bg='light grey')
label2.config(font=("Adobe Garamond Pro", 20))
var1.set('User Said:')
label2.pack()

label1 = Label(window, textvariable=var, bg='white')
label1.config(font=("Adobe Garamond Pro", 20))
var.set('(Press Play Button to give a  command)')
label1.pack()

frames = [PhotoImage(file='Assistant1.gif', format='gif -index %i' % (i)) for i in range(60)]
window.title('ALPHA ASSISTANT')
window.configure(bg='#06225F')

label = Label(window, width=50, height=50)
label.pack()
window.after(0, update, 0)

btn0 = Button(text='WISH ME', width=20, command=wishme, bg='white')
btn0.config(font=("Adobe Garamond Pro", 12))
btn0.pack(pady=2)

btn1 = Button(text='PLAY', width=20, command=play, bg='white')
btn1.config(font=("Adobe Garamond Pro", 12))
btn1.pack(pady=2)

btn2 = Button(text='EXIT', width=20, command=window.destroy, bg='white')
btn2.config(font=("Adobe Garamond Pro", 12))
btn2.pack(pady=2)

window.mainloop()
