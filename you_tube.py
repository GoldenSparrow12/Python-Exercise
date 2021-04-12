import pytube
from pytube import YouTube

user_url = input("Enter the url\n")
res = int(input("Enter Resolution 144,360,480,720,1080: "))
youtube = pytube.YouTube(user_url)
try:
    video = youtube.streams.filter(res=f'{res}p').first().download('Video_download')
except AttributeError:
    print(f"Not present in {res}p Resolution")
