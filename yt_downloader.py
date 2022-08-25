from tkinter import * 
import tkinter as tk
from pytube import YouTube
from tkinter import messagebox, filedialog

def Download_Video():
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    tk.Label(window, text = 'Your Video is downloaded!', font = 'arial 15',fg="White",bg="#EC7063").place(x= 10 , y = 140)  
 

 


window = tk.Tk()
window.geometry('600x400')
window.config(bg='#EC7063')
window.resizable(width=True,height=True)
window.title('YT Downloader')
img=PhotoImage(file='yt.png')
window.iconphoto(False, img)

link = tk.StringVar()
tk.Label(window,text='Yt Downloader', font ='arial 20 bold',fg="White",bg="Black").pack()
tk.Label(window,text='Paste you link here:', font = 'arial 20 bold',fg="Black",bg="#EC7063").place(x= 5 , y = 60)
link_enter = tk.Entry(window, width=53, textvariable= link,font = 'arial 15 bold',bg="lightgreen").place(x = 5, y = 100)
tk.Label(window,text='Paste you link here:', font = 'arial 20 bold',fg="Black",bg="#EC7063").place(x= 5 , y = 60)
tk.Button(window,text = 'DOWNLOAD VIDEO', font = 'arial 15 bold' ,fg="white",bg = 'black', padx = 2,command=Download_Video).place(x=385 ,y = 140)
tk.Label(window,text='Select Folder:', font = 'arial 20 bold',fg="Black",bg="#EC7063").place(x= 5 , y = 150)


window.mainloop()