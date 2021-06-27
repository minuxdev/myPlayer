from pygame import mixer
from TkinterDnD2 import DND_FILES, TkinterDnD
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import os


mixer.init()

master = TkinterDnD.Tk()

master.title("myPlayer")
master.minsize(250, 300)
master.resizable(False, False)
master.config(bg='black')

# Defining them (available native themes [clam, xpnative, 
# vista, classic, winnative, alt])

theme = ttk.Style()
theme.theme_use("alt")

#=================================================#
#                   VARIABLES                     #
#=================================================#

def LoadingFiles(images, songs, names):

    for root, dirs, files in os.walk(os.path.abspath(r'.')):

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
backIcon = ImageTk.PhotoImage(Image.open(os.path.abspath("./icons/back.png")))
playIcon = ImageTk.PhotoImage(Image.open(os.path.abspath("./icons/play.png")))
pauseIcon = ImageTk.PhotoImage(Image.open(
    os.path.abspath("./icons/pause.png")))
nextIcon = ImageTk.PhotoImage(Image.open(os.path.abspath("./icons/next.png")))

icount = mzk = counter = current = 0
vol = 0.9921875
iFile = iList[icount]

#=================================================#
#             CONTROL FUNCTIONS                   #
#=================================================#

def MasterShortcuts(event):
    print(event)
    if event.char == " ":
        if mixer.music.get_pos() > 0.2:
            Pause()
        else:
            Play()
    
    elif event.char == "a":
        Back()

    elif event.char == "d":
        Next()

    elif event.char == "w":
        VolumeUp(event)

    elif event.char == "s":
        VolumeDown(event)
    
    elif event.char == "l":
        Plist()


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

    global icount, iFile, mzk

    if mixer.music.get_busy():
        mixer.music.pause()

    else:
        mixer.music.unpause()


def Next():

    global icount, iFile, mzk

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


def VolumeUp(event):
    global vol
    
    if event.num == 1 or event.char == "w":

        if mixer.music.get_volume() >= 0.9899:
            vol_state = "Volume: 100%"
            freeLabel.config(text=vol_state)
        else:
            vol = mixer.music.get_volume() + 0.1
            mixer.music.set_volume(vol)
            freeLabel.config(text=f"Volume: {int(vol * 100)}%")


def VolumeDown(event):
    global vol

    if event.num == 3 or event.char == "s":
        if mixer.music.get_volume() > 0.1:
            vol -= 0.1
            mixer.music.set_volume(vol)
            freeLabel.config(text=f"Volume: {int(vol * 100)}%")
        else:
            freeLabel.config(text=f"Volume: 10%")



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

    master.after(1000, GetPos)
    time_stamp.config(
        text=f"{counter}:{current} min \t\t {mzk + 1}/{len(mList)}",
        font='Mono 8 italic', fg='white')


def EndEvent():
    global mzk

    if mixer.music.get_busy():
        pass
    else:
        # if mzk == 0:
        #     pass

        if mzk == 0 and mixer.music.get_pos() > 0.5:
            print("If statement")
            mzk += 1
            print(mzk)
            # mixer.music.load(mList[mzk])
            # mixer.music.play()

        elif mixer.music.get_pos() <= 0 and mzk + 1 < len(mList):
            if mzk == 0:
                pass
            else:
                print("Elif")
                try:
                    mixer.music.load(mList[mzk + 1])
                    mixer.music.play()
                    file_name.config(text=mzkName[mzk + 1])
                    mzk = mList.index(mList[mzk]) + 1
                
                except IndexError:
                    print("Last Song Ended")
       
        # if mzk + 1 < len(mList):
        #     mzk = mList.index(mList[mzk]) + 1

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
imgViewer.bind("<Double - 1>", VolumeUp)
imgViewer.bind("<Button - 3>", VolumeDown)

file_name = Label(nameFrame, justify="left", width=16, font='Mono 8 italic',
                  text=mzkName[mzk], bg='black', fg='white')
file_name.pack(fill='both')


time_stamp = Label(nameFrame, font='Mono 9 italic',
                   bg='black', fg='white')
time_stamp.pack(fill="x")


back = Button(ctrlFrame, image=backIcon, bg='black', bd=0, command=Back)
play = Button(ctrlFrame, image=playIcon, bg='black', bd=0, command=Play)
pause = Button(ctrlFrame, image=pauseIcon, bg='black', bd=0, command=Pause)
next_ = Button(ctrlFrame, image=nextIcon, bd=0, bg='black', command=Next)
freeLabel = Label(ctrlFrame, height=1, bd=0, bg='black')

back.grid(row=0, column=0, padx=5, pady=2, sticky='we')
play.grid(row=0, column=1, padx=5, pady=2, sticky='we')
pause.grid(row=0, column=2, padx=5, pady=2, sticky='we')
next_.grid(row=0, column=3, padx=5, pady=2, sticky='we')
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

        self.title("PlayList")
        self.minsize(width=400, height=300)
        self.grab_set()

        self.lbox = Listbox(self)
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

        for n, item in enumerate(self.name_list):
            item = f"{n+1}. {item}"
            self.lbox.insert(END, item)

    def Play_selected_song(self, event):
        try:
            song = self.lbox.curselection()[0]
            mixer.music.load(self.song_list[song])
            mixer.music.play()
            self.label_name.config(text=self.name_list[song])
        except IndexError:
            pass
    
    def Add_File(self, event):
        if ".wav" not in event.data:
            pass
        else:
            dropped = event.data[1:]
            if dropped[-1] == "}":
                print("If Statement")
                file = dropped[:-1]
            else:
                print("Else Statement")
                file = dropped

            name = file.split("/")[-1]
            mzkName.append(name)
            mList.append(file)
            self.lbox.insert("end", name)
        print(mList)
    
    def ShortCuts(self, event):
        print(event)
        item = self.lbox.curselection()[0]
        if event.char == "\x7f":
            print(item)
            self.lbox.delete(item)
            mList.pop(item)
            self.name_list.pop(item)
            print(mList)

        elif event.char == "\r":
            mixer.music.load(mList[item])
            mixer.music.play()
            self.label_name.config(text=self.name_list[item])
            mzk = self.name_list.index(mList[item])
            print(len(mzk))


master.focus()

GetPos()

EndEvent()

master.update()

master.bind("<Key>", MasterShortcuts)
master.bind("<Button 3>", MasterShortcuts)

master.mainloop()

mixer.music.stop()
