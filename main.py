import youtube_dl
import tkinter as tk

def download(url):
    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

window = tk.Tk()
window.title("Youtube Downloader")
window.geometry("500x500")

label = tk.Label(text="Enter the URL of the video you want to download")
label.pack()

entry = tk.Entry()
entry.pack()

button = tk.Button(text="Download", command=lambda: download(entry.get()))
button.pack()

# Create a label to display "Youtube"
label = tk.Label(text="Youtube", font=("Arial", 40), fg="red")
label.pack()
label = tk.Label(text="Downloader", font=("Arial", 40), fg="red")
label.pack()

window.mainloop()