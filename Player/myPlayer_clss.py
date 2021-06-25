from pygame import mixer
from TkinterDnD2 import DND_FILES, TkinterDnD
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import os

mixer.init()


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

Image_List, Songs_List, Song_Name = LoadingFiles(ImageList, SongList, NameList)

class Functions():
    def __init__(self):
        self.win = MainWindow()

        self.mzk = self.win.mzk
        self.icount = self.win.icount
        self.iFile = self.win.iFile
        self.vol = self.win.vol
        self.counter = self.win.counter
        self.mzk = self.win.mzk

        self.imgViewer = self.win.imgViewer
        self.file_name = self.win.file_name
        self.freeLabel = self.win.freeLabel
        self.mzk = self.win.mzk
        self.mzk = self.win.mzk

        self.Signals()

    def Signals(self):
        self.imgViewer.bind("<Double - 1>", self.VolumeUp)
        self.imgViewer.bind("<Button - 3>", self.VolumeDown)
    

    def Back(self):

        if self.mzk == 0:
            if self.icount == 0:
                pass
            pass

        else:
            self.mzk -= 1

            mixer.music.load(Songs_List[self.mzk])
            mixer.music.play()
            if Image_List.index(self.iFile) > 0:
                self.icount -= 1
                self.iFile = Image_List[self.icount]

        self.imgViewer.config(image=self.iFile)
        self.file_name.config(text=Song_Name[self.mzk])


    def Play(self):

        mixer.music.load(Songs_List[self.mzk])
        mixer.music.play()


    def Pause(self):

        if mixer.music.get_busy():
            mixer.music.pause()

        else:
            mixer.music.unpause()


    def Next(self):

        if Songs_List.index(Songs_List[self.mzk]) + 1 == len(Songs_List):
            pass

        else:
            try:
                self.mzk += 1
                mixer.music.load(Songs_List[self.mzk])
                mixer.music.play()
                if self.icount + 1 == len(Image_List):
                    pass
                else:
                    self.icount += 1
                    self.iFile = Image_List[self.icount]

                self.imgViewer.config(image=self.iFile)
                self.file_name.config(text=Song_Name[self.mzk])
            except IndexError:
                pass


    def VolumeUp(self, event):

        print(mixer.music.get_volume())
        
        if mixer.music.get_volume() >= 0.9899:
            vol_state = "Volume: 100%"
            self.freeLabel.config(text=vol_state)
        else:
            self.vol = mixer.music.get_volume() + 0.1
            mixer.music.set_volume(self.vol)
            self.freeLabel.config(text=f"Volume: {int(self.vol * 100)}%")

    def VolumeDown(self, event):
        print(event)
        if mixer.music.get_volume() > 0.1:
            self.vol -= 0.1
            mixer.music.set_volume(self.vol)
            self.freeLabel.config(text=f"Volume: {int(self.vol * 100)}%")
        else:
            self.freeLabel.config(text=f"Volume: 10%")


    def Plist(self):
        Top()
    

    def Quit(self):
        self.win.master.destroy()

    def Version(self):
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


    def Author(self):
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


class MainWindow:
    def __init__(self):
        self.master = TkinterDnD.Tk()
        self.master.title("myPlayer")
        self.master.minsize(250, 300)
        self.master.resizable(False, False)
        self.master.config(bg='black')

        Grid.columnconfigure(self.master, 0, weight=1)
        Grid.rowconfigure(self.master, 0, weight=1)

        self.Func = Functions()
        self.MainFunct()

    
    def MainFunct(self):
        self.LoadingButtons()
        self.Variables()
        self.FramesWidgets()
        self.Menu()


    def LoadingButtons(self):
        # Loading Icon Buttons
        self.backIcon = ImageTk.PhotoImage(Image.open(os.path.abspath("./icons/back.png")))
        self.playIcon = ImageTk.PhotoImage(Image.open(os.path.abspath("./icons/play.png")))
        self.pauseIcon = ImageTk.PhotoImage(Image.open(
            os.path.abspath("./icons/pause.png")))
        self.nextIcon = ImageTk.PhotoImage(Image.open(os.path.abspath("./icons/next.png")))


    def Variables(self):
        self.icount = self.mzk = self.counter = self.current = 0
        self.vol = 0.9921875
        self.iFile = Image_List[self.icount]


    def FramesWidgets(self):

        iFrame = Frame(self.master)
        nameFrame = Frame(self.master)
        self.ctrlFrame = Frame(self.master, bg='black', width=15, height=1)

        frames = [iFrame, nameFrame, self.ctrlFrame]

        for i in range(len(frames)):
            Grid.rowconfigure(frames[i], i, weight=1)
            Grid.columnconfigure(frames[i], i, weight=1)


        iFrame.grid(column=0, padx=20, pady=2, sticky='news')
        nameFrame.grid(column=0, padx=20, pady=2, sticky='ew')
        self.ctrlFrame.grid(column=0, padx=20, pady=2, sticky='ew')


        self.imgViewer = Label(iFrame, bg='black', image=self.iFile)
        self.imgViewer.grid(row=0, column=0, sticky='news')

        self.file_name = Label(nameFrame, font='Mono 9',
                  text=Song_Name[0], bg='black', fg='white')
        self.file_name.pack(fill='both')


        self.time_stamp = Label(nameFrame, font='Mono 9',
                        bg='black', fg='white')
        self.time_stamp.pack(fill="x")


        back = Button(self.ctrlFrame, image=self.backIcon, bg='black', bd=0, command=self.Func.Back)
        play = Button(self.ctrlFrame, image=self.playIcon, bg='black', bd=0, command=self.Func.Play)
        pause = Button(self.ctrlFrame, image=self.pauseIcon, bg='black', bd=0, command=self.Func.Pause)
        Next = Button(self.ctrlFrame, image=self.nextIcon, bd=0, bg='black', command=self.Func.Next)
        self.freeLabel = Label(self.ctrlFrame, height=1, bd=0, bg='black')

        back.grid(row=0, column=0, padx=5, pady=2, sticky='we')
        play.grid(row=0, column=1, padx=5, pady=2, sticky='we')
        pause.grid(row=0, column=2, padx=5, pady=2, sticky='we')
        Next.grid(row=0, column=3, padx=5, pady=2, sticky='we')


    def Menu(self):
        self.menuBar = Menu(self.master, bg='black', fg="white", bd=0)

        file = Menu(self.menuBar, tearoff=0)
        file.add_command(label="PlayList", command=self.Func.Plist)
        file.add_separator()
        file.add_command(label="Exit", command=self.Func.Quit)

        view = Menu(self.menuBar, tearoff=0)
        view.add_command(label="Green", command=self.Green)
        view.add_command(label="Red", command=self.Red)
        view.add_command(label="Blue", command=self.Blue)
        view.add_separator()
        view.add_command(label="Default", command=self.Default)


        about = Menu(self.menuBar, tearoff=0)
        about.add_command(label="Version", command=self.Func.Version)
        about.add_command(label="Author", command=self.Func.Author)

        self.menuBar.add_cascade(label="File", menu=file)
        self.menuBar.add_cascade(label="View", menu=view)
        self.menuBar.add_cascade(label="About", menu=about)

        self.master.config(menu=self.menuBar)


    def White(self):
        self.master.config(bg='white')
        self.ctrlFrame.config(bg="white")
        self.file_name.config(bg="white", fg="black")
        self.freeLabel.config(bg="white", fg="black")
        self.menuBar.config(bg="white", fg="black")
        self.time_stamp.config(bg="white")


    def Red(self):
        self.master.config(bg='red')
        self.ctrlFrame.config(bg="red")
        self.file_name.config(bg="red", fg="black")
        self.freeLabel.config(bg="red", fg="black")
        self.menuBar.config(bg="red", fg="black")
        self.time_stamp.config(bg="red")


    def Green(self):
        self.master.config(bg='green')
        self.ctrlFrame.config(bg="green")
        self.file_name.config(bg="green", fg="black")
        self.freeLabel.config(bg="green", fg="black")
        self.menuBar.config(bg="green", fg="black")
        self.time_stamp.config(bg="green")


    def Blue(self):
        self.master.config(bg='blue')
        self.ctrlFrame.config(bg="blue")
        self.file_name.config(bg="blue", fg="white")
        self.freeLabel.config(bg="blue", fg="white")
        self.menuBar.config(bg="blue", fg="white")
        self.time_stamp.config(bg="blue")


    def Default(self):

        self.master.config(bg='black')
        self.menuBar.config(bg='black', fg="white")
        self.ctrlFrame.config(bg="black")
        self.file_name.config(bg="black", fg="white")
        self.freeLabel.config(bg="black", fg="white")
        self.time_stamp.config(bg="black")


def GetPos():
    win = MainWindow()
    master = win.master
    time_stamp = win.time_stamp

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
        text=f"Duration: {counter}:{current} min",
        font='Mono 8 italic', fg='white')


def EndEvent():
    win = MainWindow()
    mzk = win.mzk
    master = win.master

    if mixer.music.get_busy():
        pass
    else:
        if mzk == 0:
            mixer.music.load(Songs_List[mzk])
            mixer.music.play()

        elif mixer.music.get_pos() <= 0 and mzk < len(Songs_List):
            try:
                mixer.music.load(Songs_List[mzk + 1])
                mixer.music.play()
                win.file_name.config(text=Song_Name[mzk + 1])
            except IndexError:
                print("Last Song Ended")
                # master.destroy()
        if Songs_List.index(Songs_List[mzk]) < len(Songs_List):
            mzk = Songs_List.index(Songs_List[mzk]) + 1

    master.after(1000, EndEvent)


class Top(Toplevel):
    def __init__(self):
        super().__init__()
        self.win = MainWindow()

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

        self.Play_list()

    def Play_list(self):

        self.lbox.delete(0, END)

        for n, item in enumerate(Song_Name):
            item = f"{n+1}. {item}"
            self.lbox.insert(END, item)

    def Play_selected_song(self, event):
        try:
            song = self.lbox.curselection()[0]
            mixer.music.load(Songs_List[song])
            mixer.music.play()
            self.win.file_name.config(text=Song_Name[song])
        except IndexError:
            pass
    
    def Add_File(self, event):
        if ".wav" not in event.data:
            print("File not recognized!")
            print(event.data)
        else:
            file = event.data[1:-1]
            name = file.split("/")[-1]
            Song_Name.append(name)
            Songs_List.append(file)
            self.lbox.insert("end", name)
        print(Songs_List)


if __name__ == "__main__":
    main = MainWindow()
    main.master.update()
    GetPos()
    EndEvent()
    main.master.mainloop()

    mixer.music.stop()
