import os
from pytube import YouTube
from tqdm import tqdm

def progress_function(stream, chunk, bytes_remaining):
    current = ((stream.filesize - bytes_remaining)/stream.filesize)
    bar.update(current)

print("Welcome to the FluxoSoft Video Downloader!")
print()

url = input("Enter the URL of the video you want to download!: ")
yt = YouTube(url)
yt.register_on_progress_callback(progress_function)

print("Available resolutions (Quality):")
streams = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc()
for i, stream in enumerate(streams):
    print(f"{i + 1}: {stream.resolution}")

stream_number = int(input("Enter Which quality you want to download in: ")) - 1
stream = streams[stream_number]

path = "./downloads"

# Check if directory exists, if not, create it
if not os.path.exists(path):
    os.makedirs(path)

with tqdm(total=stream.filesize, unit='B', unit_scale=True) as bar:
    stream.download(path)