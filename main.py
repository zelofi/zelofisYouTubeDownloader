import tkinter
import tkinter.messagebox
from tkinter.filedialog import askdirectory
import customtkinter

import os

from pytube import YouTube

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("theme.json")

# Functions
def download():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)

        if highestQuality.get() == True:
            video = ytObject.streams.get_highest_resolution()
        else:
            video = ytObject.streams.get_lowest_resolution()

        title.configure(text="Title: " + ytObject.title, text_color="white")
        finish.configure(text="")
        video.download(directory._text)
        finish.configure(text="Downloaded!", text_color="white")
    except:
        if ytObject.age_restricted == True:
            finish.configure(text="Download Error! Video is age restricted!", text_color="red")
        else:
            finish.configure(text="Download Error!", text_color="red")

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completetion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_completetion))
    pPercentage.configure(text=per + '%')
    pPercentage.update()

    progressBar.set(float(percentage_of_completetion) / 100)

def directoryDef():
    path = '{}'.format(askdirectory(title='Select Folder', initialdir='C:/', mustexist=True))
    directory.configure(text=path)

root = customtkinter.CTk()
root.title("zelofi's YT Downloader")
root.geometry("1280x720")
root.iconbitmap(os.path.join("src/images", "youtube.ico"))

frame_yt = customtkinter.CTkFrame(master=root, corner_radius=10)
frame_yt.pack(padx=10, pady=10)

header = customtkinter.CTkLabel(master=frame_yt, text="zelofi's YT Downloader", font=("Roboto", 36))
header.pack(padx=10, pady=10)

title = customtkinter.CTkLabel(master=frame_yt, text="Title: None!", font=("Roboto", 24))
title.pack(padx=10, pady=10)

link = customtkinter.CTkEntry(master=frame_yt, placeholder_text="YouTube Link", font=("Roboto", 12), width=420, height=50)
link.pack(padx=10, pady=10)

directory = customtkinter.CTkLabel(master=frame_yt, text="?", font=("Roboto", 12), width=420, height=50)
directory.pack(padx=10, pady=1)

directoryButton = customtkinter.CTkButton(master=frame_yt, text="Change Directory/Path", font=("Roboto", 15), width=280, height=40, command=directoryDef)
directoryButton.pack(padx=10, pady=10)

downloadButton = customtkinter.CTkButton(master=frame_yt, text="Download", font=("Roboto", 15), width=320, height=40, command=download)
downloadButton.pack(padx=10, pady=10)

highestQuality = customtkinter.CTkCheckBox(master=frame_yt, text="Highest quality?")
highestQuality.pack(padx=10, pady=10)

pPercentage = customtkinter.CTkLabel(master=frame_yt, text="0%")
pPercentage.pack(padx=10, pady=10)

progressBar = customtkinter.CTkProgressBar(master=frame_yt, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)

finish = customtkinter.CTkLabel(master=frame_yt, text="", font=("Roboto", 20))
finish.pack(padx=10, pady=10)

root.mainloop()