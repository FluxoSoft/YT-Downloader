import os
import tkinter as tk
from tkinter import ttk
from pytube import YouTube
from tqdm import tqdm

def progress_function(stream, chunk, bytes_remaining):
    current = ((stream.filesize - bytes_remaining)/stream.filesize)
    progress_bar['value'] = current * 100
    root.update_idletasks()

def download_video(url, quality):
    yt = YouTube(url)
    yt.register_on_progress_callback(progress_function)

    streams = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc()
    stream = streams[quality]

    path = "./downloads"
    if not os.path.exists(path):
        os.makedirs(path)

    stream.download(path)

def populate_qualities(url):
    yt = YouTube(url)
    streams = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc()
    qualities = [stream.resolution for stream in streams]
    quality_dropdown['values'] = qualities

root = tk.Tk()
root.title("FluxoSoft | Video Downloader")
root.configure(bg='black')

url_label = tk.Label(root, text="Enter the URL of the video:", bg='black', fg='white', font=('Arial', 14))
url_label.pack(pady=10)

url_entry = tk.Entry(root, bg='grey', font=('Arial', 12))
url_entry.pack(pady=10)

quality_label = tk.Label(root, text="Select the video quality:", bg='black', fg='white', font=('Arial', 14))
quality_label.pack(pady=10)

quality_dropdown = ttk.Combobox(root, font=('Arial', 12))
quality_dropdown.pack(pady=10)

download_button = tk.Button(root, text="Download", command=lambda: download_video(url_entry.get(), quality_dropdown.current()), bg='grey', font=('Arial', 14))
download_button.pack(pady=10)

progress_label = tk.Label(root, text="Download progress:", bg='black', fg='white', font=('Arial', 14))
progress_label.pack(pady=10)

progress_bar = ttk.Progressbar(root, orient='horizontal', length=300, mode='determinate')
progress_bar.pack(pady=10)

url_entry.bind('<Return>', lambda event: populate_qualities(url_entry.get()))

root.mainloop()
