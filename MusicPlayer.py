from logging import root
from tkinter import *
from tkinter import Tk
from tkinter import filedialog
from pygame import mixer
import os

root = Tk()
root.geometry("800x800")
root.title("Music Player")
root.configure(bg="blue")
root.resizable(False,False)
mixer.init()

def musicAdd():
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = os.listdir(path)

        for song in songs:
            if song.endswith(".mp3"):
                Playlist.insert(END, song)

def musicPlay():
    musicName = Playlist.get(ACTIVE)
    print(musicName[0:-4])
    mixer.music.load(Playlist.get(ACTIVE))
    mixer.music.play()

Button(root, width=7, height=2, bg="green", command=musicPlay) .place (x=100, y= 50)
Button(root, width=7, height=2, bg="yellow", command=mixer.music.pause) .place (x=30, y= 100)
Button(root, width=7, height=2, bg="red", command=mixer.music.stop) .place (x=100, y= 100)
Button(root, width=7, height=2, bg="orange", command=mixer.music.unpause) .place (x=170, y= 100)

Label(root, bg='white') .pack(padx=10, pady=50, side=RIGHT)
MusicFrame = Frame(root, bd=2, relief=RIDGE)
MusicFrame.place (x=300, y=350, height=200)
Button(root, text='Add Music', width=15, height=2, font='times new roman',bg='#333333', fg='black', command=musicAdd()).place(x=300, y=100)

Scroll = Scrollbar(MusicFrame)
Playlist = Listbox()

root.mainloop()