import tkinter
import tkinter.messagebox
import customtkinter
from pytube import YouTube

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("theme.json")

isOpen = False

# Functions
def download():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()

        title.configure(text="Title: " + ytObject.title, text_color="white")
        finish.configure(text="")
        video.download(directory.get())
        finish.configure(text="Downloaded!", text_color="white")
    except:
        finish.configure(text="Download Error!", text_color="red")

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completetion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_completetion))
    pPercentage.configure(text=per + '%')
    pPercentage.update()

    progressBar.set(float(percentage_of_completetion) / 100)

root = customtkinter.CTk()
root.title("zelofi's YT Downloader")
root.geometry("1280x720")

header = customtkinter.CTkLabel(master=root, text="zelofi's YT Downloader", font=("Roboto", 36))
header.pack(padx=10, pady=10)

title = customtkinter.CTkLabel(master=root, text="Title: None!", font=("Roboto", 24))
title.pack(padx=10, pady=10)

link = customtkinter.CTkEntry(master=root, placeholder_text="YouTube Link", font=("Roboto", 12), width=420, height=50)
link.pack(padx=10, pady=10)

directory = customtkinter.CTkEntry(master=root, placeholder_text="Directory", font=("Roboto", 12), width=420, height=50)
directory.pack(padx=10, pady=10)

downloadButton = customtkinter.CTkButton(master=root, text="Download", font=("Roboto", 15), width=320, height=40, command=download)
downloadButton.pack(padx=10, pady=10)

pPercentage = customtkinter.CTkLabel(root, text="0%")
pPercentage.pack(padx=10, pady=10)

progressBar = customtkinter.CTkProgressBar(root, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)

finish = customtkinter.CTkLabel(master=root, text="", font=("Roboto", 20))
finish.pack(padx=10, pady=10)

root.mainloop()