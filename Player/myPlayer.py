from pygame import mixer
from TkinterDnD2 import DND_FILES, TkinterDnD
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import os, sys
from mutagen.mp3 import MP3
from mutagen.wave import WAVE


mixer.init()

master = TkinterDnD.Tk()

master.title("myPlayer")
master.minsize(250, 300)
master.resizable(False, False)
master.config(bg='black')

#=================================================#
#                   VARIABLES                     #
#=================================================#

def LoadingFiles(images, songs, names):

    for root, dirs, files in os.walk(os.path.abspath(r'./images/')):

        for file in files:
            if '.png' in file:
                imgFile = os.path.join(root, file)
                images.append(ImageTk.PhotoImage(Image.open(imgFile)))

            elif '.wav' in file:
                mFile = os.path.join(root, file)
                path, name = os.path.split(mFile)
                songs.append(mFile)
                names.append(name)
            elif '.mp3' in file:
                mFile = os.path.join(root, file)
                path, name = os.path.split(mFile)
                songs.append(mFile)
                names.append(name)

    return images, songs, names
    

ImageList = []
SongList = []
NameList = []
iList, mList, mzkName = LoadingFiles(ImageList, SongList, NameList)

# Loading Icon Buttons
backIcon = ImageTk.PhotoImage(Image.open(os.path.abspath(r"./icons/back.png")))
playIcon = ImageTk.PhotoImage(Image.open(os.path.abspath(r"./icons/play.png")))
pauseIcon = ImageTk.PhotoImage(Image.open(
    os.path.abspath(r"./icons/pause.png")))
nextIcon = ImageTk.PhotoImage(Image.open(os.path.abspath(r"./icons/next.png")))

icount = mzk = counter = current = 0
r = 1
vol = 0.9921875
iFile = iList[icount]
ctrl = False

#=================================================#
#             CONTROL FUNCTIONS                   #
#=================================================#

def MasterShortcuts(event):
    # print(event)
    if event.char == " ":
        if mixer.music.get_pos() > 0.1:
            Pause()
        else:
            Play()
    
    elif event.char == "a":
        Back()

    elif event.char == "d":
        Next()

    elif event.num == 4 or event.char == "w":
        VolumeUp(event)

    elif event.num == 5 or event.char == "s":
        VolumeDown(event)
    
    elif event.char == "l":
        Plist()

    elif event.char == "r":
        Repeat(event)


def Back():

    global icount, iFile, mzk
    try:
        if mzk == 0:
            if icount == 0:
                pass
            pass

        else:
            mzk -= 1
            Load_Play()

            if iList.index(iFile) > 0:
                icount -= 1
                iFile = iList[icount]

        imgViewer.config(image=iFile)
    except IndexError:
        pass

def Play():
    if mList == []:
        Plist()

    else:
        mixer.music.load(mList[mzk])
        mixer.music.play()


def Pause():

    global icount, iFile, mzk

    if mixer.music.get_busy():
        mixer.music.pause()

    else:
        mixer.music.unpause()


def Next():

    global icount, iFile, mzk

    try:
        if mList.index(mList[mzk]) + 1 == len(mList):
            pass

        else:
            try:
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
            except IndexError:
                pass
            except:
                mzk -= 1
    except IndexError:
        pass

def VolumeUp(event):
    global vol
    
    if event.num == 4 or event.char == "w":

        if mixer.music.get_volume() >= 0.9899:
            vol_state = "Volume: 100%"
            freeLabel.config(text=vol_state)
        else:
            vol = mixer.music.get_volume() + 0.1
            mixer.music.set_volume(vol)
            freeLabel.config(text=f"Volume: {int(vol * 100)}%")


def VolumeDown(event):
    global vol

    if event.num == 5 or event.char == "s":
        if mixer.music.get_volume() > 0.1:
            vol -= 0.1
            mixer.music.set_volume(vol)
            freeLabel.config(text=f"Volume: {int(vol * 100)}%")
        else:
            freeLabel.config(text=f"Volume: 10%")


def Repeat(event):
    global ctrl

    if ctrl == True:
        ctrl = False
        freeLabel.config(text="Repeat Mode is off")

    elif ctrl == False:
        ctrl = True
        freeLabel.config(text="Repeat Mode is on")


#=================================================#
#             MENU BAR FUNCTIONS                  #
#=================================================#

def Plist():
    Top()


def Quit():
    master.destroy()


def Version():
    win = Tk()
    win.title("Version Info")
    win.minsize(200, 100)

    ver = '''
Name: myPlayer
Version: 0.9
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
    file_name.config(bg="green", fg="white")
    freeLabel.config(bg="green", fg="white")
    menuBar.config(bg="green", fg="white")
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
def Load_Play():
    global mzk
    try:
        mixer.music.load(mList[mzk])
        mixer.music.play()
        file_name.config(text=mzkName[mzk])
    except:
        mzk += 1

def Length(mzk):
    try:
        f = mList[mzk]
        if ".mp3" in f:
            audio = MP3(f)
        else:
            audio = WAVE(f)

        song_length = (int(audio.info.length) // 60)
        song_length = f"{song_length}.{int(audio.info.length) % 60}"

        return float(song_length)

    except IndexError:
        pass    


def GetPos():
    global counter, current

    if mixer.music.get_pos() == -1:
        time = 0
    else:
        time = mixer.music.get_pos() // 1000

    song_length = Length(mzk)

    if time == 0:
        counter = current = 0

    elif time % 60 == 0:

        counter += 1
        current = 0

    if mixer.music.get_busy():
        current += 1

    if mList == []:
        m = 0
    elif len(mList) == 1:
        m = 1
    else:
        m = mzk + 1
    
    print(f"Current time: {counter}:{current}")

    time_stamp.config(
        text=f"{counter}:{current} / {song_length} min \t\t {m}/{len(mList)}",
        font='Mono 8 italic', fg='white')

    master.after(1000, GetPos)  


def EndEvent():
    global mzk, r

    if mixer.music.get_busy():
        pass

    else:   
        if mixer.music.get_pos() <= 0 and mzk + 1 < len(mList):
            if r == 0:
                mzk = 0
            else:
                mzk = mList.index(mList[mzk]) + 1
                Load_Play()

    if ctrl is True:
        if mzk + 1 == len(mList) and mixer.music.get_pos() > 0:
            r = 0

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

if mzkName == []:
    j = "No song playing"
else:
    j = mzkName[mzk]

file_name = Label(nameFrame, width=16, font='Mono 8 italic',
                  text=j, bg='black', fg='white')
file_name.pack(fill='both')


time_stamp = Label(nameFrame, font='Mono 9 italic',
                   bg='black', fg='white')
time_stamp.pack(fill="x")


back = Button(ctrlFrame, image=backIcon, bg='black', bd=0, command=Back)
play = Button(ctrlFrame, image=playIcon, bg='black', bd=0, command=Play)
pause = Button(ctrlFrame, image=pauseIcon, bg='black', bd=0, command=Pause)
next_ = Button(ctrlFrame, image=nextIcon, bd=0, bg='black', command=Next)
freeLabel = Label(ctrlFrame, height=1, bd=0, bg='black',text="Made by Minux_Dev",
    fg="white")

back.grid(row=0, column=0, padx=5, pady=2)
play.grid(row=0, column=1, padx=5, pady=2)
pause.grid(row=0, column=2, padx=5, pady=2)
next_.grid(row=0, column=3, padx=5, pady=2)
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
menuBar.add_cascade(label="Help", menu=about)

master.config(menu=menuBar)


#==================================================#
#          TOPLEVEL & LISTBOX WIDGET               #
#==================================================#

class Top(Toplevel):
    def __init__(self):
        super().__init__()

        self.title("PlayList")
        self.minsize(width=450, height=400)
        self.grab_set()

        self.lbox = Listbox(self, selectmode="extended")
        self.lbox.grid(padx=5, pady=5, sticky="news")

        Grid.rowconfigure(self, 0, weight=1)
        Grid.columnconfigure(self, 0, weight=1)

        self.lbox.bind("<Double 1>", self.Play_selected_song)

        self.lbox.drop_target_register(DND_FILES)
        self.lbox.dnd_bind("<<Drop>>", self.Add_File)
        self.lbox.bind("<Key>", self.ShortCuts)

        self.Play_list()


    def Play_list(self):

        self.lbox.delete(0, END)

        for n, item in enumerate(mzkName):
            item = f"{n+1}. {item}"
            self.lbox.insert(END, item)


    def Play_selected_song(self, event):
        global mzk

        mzk = self.lbox.curselection()[0]
        Load_Play()


    def Add_File(self, event):
        if ".mp3" not in event.data:
            if ".wav" not in event.data:
                folder = event.data
                self.Add_Folder(folder)
            else:
                self.Mp3_Wave_File(event)
        else:
            self.Mp3_Wave_File(event)


    def Mp3_Wave_File(self, event):
            dropped = event.data[1:]        
            if dropped[-1] == "}":
                file = dropped[:-1]
            else:
                file = dropped

            name = file.split("/")[-1]
            mzkName.append(name)
            mList.append(file)
            self.lbox.insert("end", name)


    def Add_Folder(self, folder):
        global mzk

        for root, dirs, files in os.walk(folder):
            for file in files:
                if ".mp3" in file:
                    mzkName.append(file)
                    self.lbox.insert("end", file)
                    file = os.path.join(root, file)
                    mList.append(file)
                elif ".wav" in file:
                    mzkName.append(file)
                    self.lbox.insert("end", file)
                    file = os.path.join(root, file)
                    mList.append(file)
                else:
                    pass
        
            
    def ShortCuts(self, event):
        global mzk
        # print(event)

        mzk = self.lbox.curselection()[0]

        if event.char == "\x7f" or event.keysym == "Delete":
            self.lbox.delete(mzk)
            mList.pop(mzk)
            mzkName.pop(mzk)

            if mList == []:
                mixer.music.stop()
                time_stamp.config(
                    text=f"0:00 min \t\t 0/0",
                    font='Mono 8 italic', fg='white')

        elif event.char == "\r":
            Load_Play()

        elif event.char == "l":
            pass

        else:
            MasterShortcuts(event)


GetPos()

EndEvent()

master.focus()

master.update()

if sys.platform == "Linux":
    master.bind("<Button 4>", MasterShortcuts)
    master.bind("<Button 5>", MasterShortcuts)
else:
    pass
    master.bind("<MouseWheel>", MasterShortcuts)

master.bind("<Key>", MasterShortcuts)

master.mainloop()

mixer.music.stop()
