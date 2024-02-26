import speech_recognition as sr
import pyttsx3
import webbrowser
from hacked import *
from weather import *
recn = sr.Recognizer()
def take():
    with sr.Microphone() as source:
        print("leasniing")
        recn.adjust_for_ambient_noise(source)
        audio=recn.listen(source)
        text2=recn.recognize_google(audio)
        print(text2)
        return text2.lower()
def tts(text):
    eng=pyttsx3.init()
    eng.say(text)
    eng.runAndWait()
webs = [
    "SNAPCHAT","youtube"
    ,"google","instagram","telegram",
    "TIKTOK","PINTEREST","TWITTER","FACEBOOK","LINKEDIN",
    "TUMBLR",
    "VSCO",
    "FLICKR",
    "IMGUR",
    "WEHEARTIT",
    "500PX",
    "ELLO",
    "EYEEM",
    "PICSART",
    "DEVIANTART",
    "BEHANCE",
    "DRIBBBLE",
    "PHOTOBUCKET",
    "PEACH"
]
cities = [
    "Mumbai",
    "Delhi",
    "Bangalore",
    "Kolkata",
    "Chennai",
    "Hyderabad",
    "pune",
    "Ahmedabad",
    "Jaipur",
    "Surat",
    "Lucknow",
    "Kanpur",
    "Nagpur",
    "Patna",
    "Indore",
    "Thane",
    "Bhopal",
    "Visakhapatnam",
    "Vadodara",
    "Ghaziabad"
]

while True:
    
    try: 
        text=take()
    except:
        text=input("enter any text: ")  
    try:
        if "open" in text:
            for web in webs:
                if web.lower() in text:
                    webbrowser.open(f"https://www.{web.lower()}.com")
                    tts(f"open {web}")
            # tts(f"open to {text} searched {my_list[1]}")
        elif "search".lower() in text.lower():
            pass
        elif "stop" in text:
            break
        elif "start hack" in text:
            hack_in_process()
        elif "weather" in text:
            for city in cities:
                if city.lower() in text:
                    print(city)
                    tts(f'in {city} temprature is {get_current_weather(city.lower())}')
    except ValueError:
        print("try again")