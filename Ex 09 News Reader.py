""" This program are read the top 10 news and
    Give the link for more information of the news."""

from win32com.client import Dispatch
import requests


def Speak(st):
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(st)


data = requests.get('http://newsapi.org/v2/top-headlines?country=in&apiKey=385905c1683243b1a70e17f635019c9e')
news_py = data.json()
news_art = news_py["articles"]
Speak("Welcome To the News Reader")
Speak("Here Are the top 10 news for india")
Speak("So our 1st news")
for i in range(1, 11):
    print(i)
    print(news_art[i]['title'])
    Speak(news_art[i]['title'])
    print(f"For More Details:{news_art[i]['url']}")
    if i >= 10:
        break
    if i == 9:
        Speak("so our last news for today")
    else:
        Speak("Moving to the next news")
Speak("Thanks for listening! Have a nice day")
Speak("keep reading")
