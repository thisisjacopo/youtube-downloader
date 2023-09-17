from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)

print(f'Title: {yt.title}')
print(f'Number of views: {yt.views}')
print(f'Length of video: {yt.length} seconds')
print(f'Rating of video: {yt.rating}')

yd = yt.streams.get_highest_resolution()

yd.download('./downloads')