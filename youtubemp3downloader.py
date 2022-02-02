from tkinter import *
from tkinter.ttk import Progressbar
from pytube import *
import glob
import os

#Initialize Main window
main_window = Tk()
main_window.title("Youtube Downloader")
main_window.geometry("350x120")

#Create Frames
youtube_url_frame = LabelFrame(main_window, text = "Url", pady=10, padx=10)

#Position Frame
youtube_url_frame.pack()

def set_progress(progress = 0):
    progress_bar['value'] = progress
    main_window.update_idletasks()
    return 0

def download():
    print("Downloading...")
    set_progress(25)
    video = YouTube(url_form.get()).streams.filter(only_audio=True).first().download(output_path="./Downloads")
    set_progress(50)

    mp4_file_path = ""
    for name in glob.glob("Downloads" + "/**/*.mp4", recursive = True):
        mp4_file_path = name

    mp3_file_path = mp4_file_path.replace(".mp4", ".mp3")

    if os.path.isfile(mp3_file_path):
        print("File Exists")
    else:
        os.rename(mp4_file_path, mp3_file_path)

    set_progress(100)
    #Generate Completion Window
    complete_window = Tk()
    complete_message = Label(complete_window, text = "Download Complete")
    complete_message.pack()
    complete_window.mainloop()
    return 0

#Create Widgets and Forms
url_form = Entry(youtube_url_frame, width = 50)
download_button = Button(main_window, text = "Download", command = download)
progress_bar = Progressbar(main_window, orient=HORIZONTAL, length=320)

#Position Forms and Widgets
url_form.pack()
download_button.pack()
progress_bar.pack(pady = 10)

#Await user input
main_window.mainloop()
