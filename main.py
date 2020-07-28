import youtube_dl
import tkinter as tk

opts = {'outtmpl':'./videos/%(title)s.%(ext)s',}

def ytdl(x):
    with youtube_dl.YoutubeDL(opts) as y:
        t = y.download([x])

box = tk.Tk()
box.title("Youtube downloader")
box.geometry('300x70')

url = tk.Entry(box)
url.pack(padx=5,pady=5)

def ytl():
    v = url.get()
    url.delete(0,"end")
    if len(v) != 0:
        ytdl(v)
    else:
        print("not done!!")

down = tk.Button(box, text="Download", command = ytl)
down.pack(padx=5,pady=5)

box.mainloop()

