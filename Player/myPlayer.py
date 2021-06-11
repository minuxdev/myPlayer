from pygame import mixer
from tkinter import *
from PIL import ImageTk, Image
import os


mixer.init()

master = Tk()
master.title("myPlayer")
master.minsize(250, 300)
master.resizable(False, False)
master.config(bg='black')

#=================================================#
#                   VARIABLES                     #
#=================================================#

iDir = os.path.abspath(r'.')

print(iDir)

iList = []
mList = []
mzkName = []
ic = []

for root, dirs, files in os.walk(iDir):

    for file in files:
        if '.png' in file:
            imgFile = os.path.join(root, file)
            iList.append(ImageTk.PhotoImage(Image.open(imgFile)))

        elif '.wav' in file:
            mFile = os.path.join(root, file)
            path, name = os.path.split(mFile)
            mList.append(mFile)
            mzkName.append(name)
        elif '.mp3' in file:
            mFile = os.path.join(root, file)
            path, name = os.path.split(mFile)
            mList.append(mFile)
            mzkName.append(name)


# Loading Icon Buttons
backIcon = ImageTk.PhotoImage(Image.open(os.path.abspath("./icons/back.png")))
playIcon = ImageTk.PhotoImage(Image.open(os.path.abspath("./icons/play.png")))
pauseIcon = ImageTk.PhotoImage(Image.open(
    os.path.abspath("./icons/pause.png")))
nextIcon = ImageTk.PhotoImage(Image.open(os.path.abspath("./icons/next.png")))


icount = mzk = counter = current = 0

iFile = iList[icount]


#=================================================#
#             CONTROL FUNCTIONS                   #
#=================================================#

def Back():

    global icount, iFile, mzk

    if mzk == 0:
        if icount == 0:
            pass
        pass

    else:
        mzk -= 1

        mixer.music.load(mList[mzk])
        mixer.music.play()
        if iList.index(iFile) > 0:
            icount -= 1
            iFile = iList[icount]

    imgViewer.config(image=iFile)
    file_name.config(text=mzkName[mzk])


def Play():

    mixer.music.load(mList[mzk])
    mixer.music.play()


def Pause():
    GetPos()
    global icount, iFile, mFile, mzk

    if mixer.music.get_busy():
        mixer.music.pause()

    else:
        mixer.music.unpause()


def Next():

    global icount, iFile, mFile, mzk

    if mList.index(mList[mzk]) + 1 == len(mList):
        pass

    else:
        mzk += 1
        mixer.music.load(mList[mzk])
        mixer.music.play()
        if icount + 1 == len(iList):
            pass
        else:
            icount += 1
            iFile = iList[icount]

        imgViewer.config(image=iFile)
        file_name.config(text=mzkName[mzk])


#=================================================#
#             MENU BAR FUNCTIONS                  #
#=================================================#

def Plist():
    Top(mList, mzkName, file_name)


def Quit():
    master.destroy()


def Version():
    win = Tk()
    win.title("Version Info")
    win.minsize(200, 100)

    ver = '''
Name: myPlayer
Version: 0.1
Code Date: Jun 09 2021
Languages: English UK
Coded in: Python & Tkinter

    '''

    Message(win, justify="left", font="Mono 10 italic",
            text=ver, anchor="w").pack()


def Author():
    win = Tk()
    win.title("Version Info")
    win.minsize(200, 100)

    ver = '''
Author Name: Minux
Company: Minux_Dev Inc.

Is an authodidate programmer
who is still learning the basics
about programming in general.

    '''

    Message(win, justify="left", font="Mono 10 italic",
            text=ver, anchor="w").pack()


def White():
    master.config(bg='white')
    ctrlFrame.config(bg="white")
    file_name.config(bg="white", fg="black")
    freeLabel.config(bg="white", fg="black")
    menuBar.config(bg="white", fg="black")
    time_stamp.config(bg="white")


def Red():
    master.config(bg='red')
    ctrlFrame.config(bg="red")
    file_name.config(bg="red", fg="black")
    freeLabel.config(bg="red", fg="black")
    menuBar.config(bg="red", fg="black")
    time_stamp.config(bg="red")


def Green():
    master.config(bg='green')
    ctrlFrame.config(bg="green")
    file_name.config(bg="green", fg="black")
    freeLabel.config(bg="green", fg="black")
    menuBar.config(bg="green", fg="black")
    time_stamp.config(bg="green")


def Blue():
    master.config(bg='blue')
    ctrlFrame.config(bg="blue")
    file_name.config(bg="blue", fg="white")
    freeLabel.config(bg="blue", fg="white")
    menuBar.config(bg="blue", fg="white")
    time_stamp.config(bg="blue")


def Default():

    master.config(bg='black')
    menuBar.config(bg='black', fg="white")
    ctrlFrame.config(bg="black")
    file_name.config(bg="black", fg="white")
    freeLabel.config(bg="black", fg="white")
    time_stamp.config(bg="black")


#=================================================#
#              FUNCTIONS IN LOOP                  #
#=================================================#
def GetPos():
    global counter, current

    time = mixer.music.get_pos() // 1000

    if time == 0:
        counter = current = 0

    elif time % 60 == 0:

        counter += 1
        current = 0

    if mixer.music.get_busy():
        current += 1
    else:
        pass

    master.after(1000, GetPos)
    time_stamp.config(
        text=f"Duration: {counter}:{current} min",
        font='Mono 8 italic', fg='white')


def EndEvent():
    global mzk
    # print(mixer.music.get_endevent())
    if mixer.music.get_busy():
        pass
    else:
        if mzk == 0:
            mixer.music.load(mList[mzk])
            mixer.music.play()

        elif mixer.music.get_pos() <= 0 and mzk < len(mList):
            try:
                mixer.music.load(mList[mzk + 1])
                mixer.music.play()
                file_name.config(text=mzkName[mzk])
            except IndexError:
                print("Last Song Ended")
                master.destroy()

        mzk = mList.index(mList[mzk]) + 1

    master.after(1000, EndEvent)


#==================================================#
#              FRAMES AND WIDGETS                  #
#==================================================#

iFrame = Frame(master)
nameFrame = Frame(master)
ctrlFrame = Frame(master, bg='black', width=15, height=1)


# Placing frames into master window
Grid.columnconfigure(master, 0, weight=1)
Grid.rowconfigure(master, 0, weight=1)

frames = [iFrame, nameFrame, ctrlFrame]

for i in range(len(frames)):
    Grid.rowconfigure(frames[i], i, weight=1)
    Grid.columnconfigure(frames[i], i, weight=1)


iFrame.grid(column=0, padx=20, pady=2, sticky='news')
nameFrame.grid(column=0, padx=20, pady=2, sticky='ew')
ctrlFrame.grid(column=0, padx=20, pady=2, sticky='ew')


imgViewer = Label(iFrame, bg='black', image=iFile)
imgViewer.grid(row=0, column=0, sticky='news')

file_name = Label(nameFrame, font='Mono 9',
                  text=mzkName[0], bg='black', fg='white')
file_name.pack(fill='both')


time_stamp = Label(nameFrame, font='Mono 9',
                   bg='black', fg='white')
time_stamp.pack(fill="x")


back = Button(ctrlFrame, image=backIcon, bg='black', bd=0, command=Back)
play = Button(ctrlFrame, image=playIcon, bg='black', bd=0, command=Play)
pause = Button(ctrlFrame, image=pauseIcon, bg='black', bd=0, command=Pause)
Next = Button(ctrlFrame, image=nextIcon, bd=0, bg='black', command=Next)
freeLabel = Label(ctrlFrame, height=1, bd=0, bg='black')

back.grid(row=0, column=0, padx=5, pady=2, sticky='we')
play.grid(row=0, column=1, padx=5, pady=2, sticky='we')
pause.grid(row=0, column=2, padx=5, pady=2, sticky='we')
Next.grid(row=0, column=3, padx=5, pady=2, sticky='we')
freeLabel.grid(row=1, column=0, columnspan=4, sticky='news')


#==================================================#
#                   MENU BAR                       #
#==================================================#
menuBar = Menu(master, bg='black', fg="white", bd=0)

file = Menu(menuBar, tearoff=0)
file.add_command(label="PlayList", command=Plist)
file.add_separator()
file.add_command(label="Exit", command=Quit)

view = Menu(menuBar, tearoff=0)
# view.add_command(label="White", command=White)
view.add_command(label="Green", command=Green)
view.add_command(label="Red", command=Red)
view.add_command(label="Blue", command=Blue)
view.add_separator()
view.add_command(label="Default", command=Default)


about = Menu(menuBar, tearoff=0)
about.add_command(label="Version", command=Version)
about.add_command(label="Author", command=Author)

menuBar.add_cascade(label="File", menu=file)
menuBar.add_cascade(label="View", menu=view)
menuBar.add_cascade(label="About", menu=about)

master.config(menu=menuBar)


#==================================================#
#          TOPLEVEL & LISTBOX WIDGET               #
#==================================================#

class Top(Toplevel):
    def __init__(self, song_list, name_list, label_name):
        super().__init__()

        self.song_list = song_list
        self.name_list = name_list
        self.label_name = label_name

        self.config(width=400, height=300)
        self.grab_set()

        self.lbox = Listbox(self)
        self.lbox.grid(padx=5, pady=5, sticky="news")

        Grid.rowconfigure(self, 0, weight=1)
        Grid.columnconfigure(self, 0, weight=1)

        self.lbox.bind("<Double 1>", self.Play_selected_song)

        self.Play_list()

    def Play_list(self):

        self.lbox.delete(0, END)

        for n, item in enumerate(self.name_list):
            item = f"{n}. {item}"
            self.lbox.insert(END, item)

    def Play_selected_song(self, event):

        print(event)
        song = self.lbox.curselection()[0]
        mixer.music.load(self.song_list[song])
        mixer.music.play()
        self.label_name.config(text=self.name_list[song])


GetPos()

EndEvent()


master.mainloop()

mixer.music.stop()
