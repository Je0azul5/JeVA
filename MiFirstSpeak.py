#Author: Je0azul5

# Se importa Pyttx3 pip install pyttsx3
import pyttsx3
# IMportamos la biblioteca de fecha
import datetime
# Importamos reconocimiento de voz  pip install speechRecognition
import speech_recognition as sr
# IMportamos la biblioteca de wikipedia
import wikipedia  # pip install wikipedia
# SMTP protocol client
import smtplib
# Buscaddor Web
import webbrowser as wb
# Utilidades
import psutil  # pip install psutil
# Chistes malos
import pyjokes  # pip install pyjokes
# chistes perversos
import chistesESP  # pip install chistesESP
# operating system
import os
# screenshot
import pyautogui  # pip install pyautogui
#ramdom
import random
#instalar wolframalpha
import wolframalpha #pip install wolframalpha
#Read JSON
import json
#request
import requests
#url request
from urllib.request import urlopen


# Inicializamos pyttsx3
engine = pyttsx3.init()

# Funcion para recoger el texto
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Saludo
#speak("Hi my lora")
# Funcion para saber la hora


def time_():
    # "%I:%M:%S" formato 12 horas con segundos
    # "%H:%M:%S" formato 24 horas con segundos
    Time = datetime.datetime.now().strftime("%H:%M")
    speak("the time is:")
    speak(Time)


# Me dice la hora
# time_()

# Funcion para saber la fecha
def date_():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    speak("Day ")
    speak(day)
    speak("Of mounth ")
    speak(month)
    speak("in the year")
    speak(year)

# Me dice la fecha DD/MM/AA
# date_()

# Accion de regreso resumen
def wishme():

    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak(" Good Morning, I miss you JE, welcome back")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon, I miss you JE, welcome back")
    elif hour >= 18 and hour < 24:
        speak("Good evening, I miss you JE, welcome back")
    else:
        speak("Good night I, miss you JE, welcome back")

    speak("Im to your server, Tell me how can I help u? ")
    # Definimos el saludo
    # time_()
    # date_()


# Me da un resumen sin reconocimiento de voz
# wishme()

# Reconocimiento de voz
def TakeComand():
    # Se asocia el reonocedor
    r = sr.Recognizer()
    # Agregamos el microfono
    with sr.Microphone() as source:
        print("I´m listen you")
        r.pause_threshold = 1
        # Escuchamos el microfono
        audio = r.listen(source)

    try:
        # using the Google Speech Recognition API.
        print("Listening.....")
        query = r.recognize_google(audio, language='en-US')  # en-US
        print(query)
        # speak(query)
    except Exception as e:
        print(e)
        speak("Can u repeat again, please ")
        return "None"
    return query

#Nombre 
def Myname_():
    speak("My name is Pending")

# Reconociento de voz
# TakeComand()

# Envio de Email
def sendEmail_(to, content):
    server = smtplib.SMTP('64.233.184.108')
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login("usr@gmail.com", "pss")
    server.sendmail("usr@gmail.com", to, content)
    server.close()


# info cpu
def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at '+usage)

# info weather
def temperatures():
    temperatures = psutil.sensors_fans()
    speak('Weather is at '+temperatures)

# info bateria porcentaje
def battery():
    baterry = psutil.sensors_battery()
    speak('Battery is at '+baterry)

# Cuenta chistes
def jokes():
    a = chistesESP.get_random_chiste()
    print(a)
    speak(a)

# Screenshot
def screenshot():
    img = pyautogui.screenshot()
    img.save('C:/Users/Usuario/Documents/Jarvis/Images/screen'+datetime.datetime.now().strftime("%H_%M") +
             '_m'+str(datetime.datetime.now().month)+'d_'+str(datetime.datetime.now().day)+'.png')

#Funcion main
if __name__ == "__main__":
    wishme()
    wikipedia.set_lang("es")
    while True:
        # Escribe todo en minuscula
        query = TakeComand().lower()
        # Peticiones
        # time me da la hora
        if 'time' in query:
            time_()
        # date retorna la fecha
        elif 'date' in query:
            date_()

        # Da el nombre
        elif 'give me your name' in query:
            Myname_()
        # Busca en Wikipedia
        elif 'wikipedia' in query:
            try:
                speak("Wait me Im searching")
                query = query.replace('wikipedia', '')
                result = wikipedia.summary(query, sentences=4)
                speak('According to Wikipedia this I found')
                print(result)
                speak(result)
            except Exception as e:
                speak("Im so sorry i dont understand you")
        # envia un emeail revisar el servidor
        elif 'send email' in query:
            try:
                speak('what should I say?')
                content = TakeComand()
                speak('who is the receiver?')
                reciever = input("Email address is... ")
                to = reciever
                sendEmail_(to, content)
                speak('Email Sent')
            except Exception as e:
                print(e)
                speak("Unable to send email ")
        # Busca en el navegador
        elif 'search in firefox' in query:
            speak(' What would you like search?')
            firefoxPath = 'C:/Program Files/Firefox Developer Edition/firefox.exe %s'
            searching = TakeComand().lower()
            wb.get(firefoxPath).open_new_tab(
                'https://www.google.com/search?q='+searching)
        # Abre spotify en el navegador
        elif 'search in spotify' in query:
            speak(' What would you like search?')
            firefoxPath = 'C:/Program Files/Firefox Developer Edition/firefox.exe %s'
            searching = TakeComand().lower()
            wb.get(firefoxPath).open_new_tab(
                'https://open.spotify.com/search/'+searching)
        # Abre youtube en el navegador
        elif 'search in youtube' in query:
            speak(' What would you like search?')
            firefoxPath = 'C:/Program Files/Firefox Developer Edition/firefox.exe %s'
            searching = TakeComand().lower()
            wb.get(firefoxPath).open_new_tab(
                'https://www.youtube.com/results?search_query='+searching)
        # Dice porvcentajes de cpu
        elif 'cpu' in query:
            cpu()
            # temperatures()
            # en mi caso no aplica el porcentaje de bateria
            # battery
        # cuenta chistes perversos
        elif 'tell me a joke' in query:
            jokes()
        # Se apaga
        elif 'go offline' in query:
            speak('I miss you, i dont want to go again the dark')
            quit()

        # abre microsoft word
        elif 'open microsoft w' in query:
            speak('Openning')
            word = r'C:/Program Files/Microsoft Office/root/Office16/WINWORD.EXE'
            os.startfile(word)
        # Abre aplicacion de spotify
        elif 'open spotify' in query:
            speak('Openning')
            sp = r'spotify'
            os.startfile(sp)

        # Escribe un nota
        elif 'note note' in query:
            speak("What do you want write JE?")
            strTime = datetime.datetime.now().strftime("%H_%M")
            file = open('note/note'+strTime+'_m'+str(datetime.datetime.now().month) +
                        'd_'+str(datetime.datetime.now().day)+'.txt', 'w')
            file.write(strTime)
            try:
                print('writing ypur note')
                ans = TakeComand()
                file.write(' '+ans)
            except Exception as e:
                speak('Repeat the Command')
        
        #toma screenshot 
        elif 'take a screenshot' in query:
            speak('Smile')
            screenshot()
            speak('You know how to pose')

        #Crea recordatorios
        elif 'remember me' in query:
            speak('What would I remember you?')
            mm = TakeComand()
            speak('I remember this... '+mm)
            remem = open('assets/memo'+datetime.datetime.now().strftime("%H_%M")+'_m'+str(
                datetime.datetime.now().month)+'d_'+str(datetime.datetime.now().day)+'.txt', 'w')
            remem.write(mm)
            remem.close()
        
        #investiga noticias en https://newsapi.org/
        elif 'news' in query:
            try:
                jsonObj= urlopen("https://newsapi.org/v2/everything?q=apple&from=2021-03-29&to=2021-03-29&sortBy=popularity&apiKey=APIKEY")
                data=json.load(jsonObj)
                i=1
                speak('I found this')
                for item in data['articles']:
                    print(i,' ',item['title'])
                    print(item['description']+'\n')
                    speak(str(i)+' '+item['title'])
                    i+=1
            except Exception as e:
                print(e)
