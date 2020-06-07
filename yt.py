from pytube import YouTube
link=input()
yt=YouTube(link).streams[0]

yt.download("/home/jai/Documents/python_codes/youtubedownloader")