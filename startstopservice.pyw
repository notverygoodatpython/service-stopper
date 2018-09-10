import os #import the functionality for system commands
from tkinter import * #import tkinter (GUI)

master = Tk()
saicon = PhotoImage(file="start.gif") #define the icons
sticon = PhotoImage(file="stop.gif") 
def callback():
    os.system("nircmd elevate stopservice.bat") #define the commands when buttons are pressed: use nircmd tool to run the file as admin and trigger UAC
def callbock():
    os.system("nircmd elevate startservice.bat")
    
separator = Frame(height=10, bd=10, relief=SUNKEN) #add the top separator
separator.pack(fill=X, padx=10, pady=20)

b = Button(master, borderwidth=5, compound=LEFT, image=sticon, relief="raised", text="Stop", overrelief="sunken", command=callback) #add the top button: border = 5px, the icon is to the left of the text, the image is sticon (defined above), it has a raised border, the text is "stop", when the cursor hovers over it, it changes to sunken, the command is "callback" (defined above)
b.pack()

separator = Frame(height=10, bd=10, relief=SUNKEN)
separator.pack(fill=X, padx=10, pady=20)

c = Button(master, borderwidth=5, compound=LEFT, image=saicon, relief="raised", text="Start", overrelief="sunken", command=callbock)
c.pack()

separator = Frame(height=10, bd=10, relief=SUNKEN)
separator.pack(fill=X, padx=10, pady=20)

mainloop()

