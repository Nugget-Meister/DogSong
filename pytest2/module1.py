from ast import Str
import tkinter as tk
from tkinter.constants import DISABLED, NONE
import tkinter.font as tkFont
import sys

from tkinter import StringVar, Toplevel, ttk
from tkinter import filedialog as fd
from tkinter import messagebox

from tkinter.messagebox import showinfo
from typing import Counter, Text

import module2 as debug
from module3 import loadSongList

#Set width for widgets that require it
widgetWidth = 30

selectIndex = [None]        # Initialize array for the Selecting container
indexSize = 10              # Amount of entries to show

indexStart = 0


#Initialize empty container for windows, unsure if necessary
activeWindow = None

#load it up
songIndex = loadSongList()

#Initialize array container to hold songs 
testSong = [None] * len(songIndex)

############    


##########


class component_songSelector:

    # I create the song selectors as a class so that I can instantiate it several times.
    # More work initially but scales.

    def __init__(self, frame, count):
        ##Create Widgets
        #open button   


        
        self.label_songName        = tk.Label(frame, text = "Selected song", width = widgetWidth, anchor='w')
        self.text_songNameChosen  = tk.Label(frame, width = widgetWidth, anchor='w', text = "")

        # Using a lambda to prevent the function from being called prematurely
        self.button_openFile = ttk.Button(frame,text='...', width=3, command= lambda: select_file(count, self))
        self.button_openWindow = ttk.Button(frame,text='?', width=3, command= lambda: openSongDetails(testSong[count])) 



        # Widget placement

        self.label_songName.grid(row=count, column=0)
        self.text_songNameChosen.grid(row=count, column=1)
        self.button_openFile.grid(row=count, column=2)
        self.button_openWindow.grid(row=count,column=3)

def populateSelector(size, container, testSong, indexCur):

  #initialize container for selector objects
  container = [None] * size
  count = 0


  while (count<=size-1):  
        mod = count+indexCur    

        #create container for all objects
        if mod < len(songIndex):
            container[count] = component_songSelector(frame, count)
        
        #Grabs the name of the song and replaces dummy label
        #print(mod)
        if mod < len(songIndex):
            container[count].label_songName.config(text=songIndex[mod], anchor='w')

            if testSong[mod] != None:
                container[count].text_songNameChosen.config(text=testSong[mod].inputFile)
        
        count = count+1

  #print(container) 
  #print(songIndex)
  return container

class window_Main:

    def __init__(self, frame):
            # Initialize 
            self.text_Title = tk.Label(frame, width=10, anchor='w', text = 'DDMOD')
            self.text_Desc = tk.Label(frame, width=10, anchor='w', text = "Put the music in the game.", justify='center')
            self.button_openSelectorWindow = tk.Button(frame, text='Open DDMOD', command=lambda:openSelectorWindow())

            # Widget Placement
            self.text_Title.grid(row=0, column=2)
            self.text_Desc.grid(row=1, column=2)
            self.button_openSelectorWindow.grid(row=3, column=2)
            self.button_openSelectorWindow.grid(row=3, column=2)

class window_songSelector:

    def __init__(self,frame):

        populateSelector(indexSize, selectIndex, testSong, indexStart)

        self.button_Return = ttk.Button(frame, width=10, text='< back' ,command=lambda:openMainWindow())
        self.button_nextPage = ttk.Button(frame, width=5, text='>', command=lambda:incrementTen())
        self.button_prevPage = ttk.Button(frame, width=5, text='<', command=lambda:decrementTen())

        self.button_Return.grid(row = indexSize, column = 0)
        self.button_nextPage.grid(row = indexSize, column = 1)
        self.button_prevPage.grid(row = indexSize, column = 2)
       
        if indexStart >= len(songIndex)-10:
            self.button_nextPage.config(state = DISABLED)

        if indexStart <= 0:
            #indexStart = 0
            self.button_prevPage.config(state = DISABLED)





#### Window Transitions

def openSelectorWindow():  
    clearWindow()
    window_songSelector(frame)

def openMainWindow():
    clearWindow()
    window_Main(frame)

 
#Opens New window with song details
def openSongDetails(song):
    songDetailsWindow = Toplevel(root)
    songDetailsWindow.title('Song Details')
    songDetailsWindow.geometry('300x250')
    frame_songWindow = tk.Frame(songDetailsWindow)

    songDetailWidth = 20

    #Initialize labels
    label_songNameChosen  = tk.Label(frame_songWindow, anchor='e', width = songDetailWidth, text = "File Name:")
    label_songSampleRate = tk.Label(frame_songWindow, anchor='e', width = songDetailWidth, text =  "Sample Rate:")
    label_songBitrateType = tk.Label(frame_songWindow, anchor='e', width = songDetailWidth, text = "Bitrate Type:")
    label_songLength = tk.Label(frame_songWindow, anchor='e', width = songDetailWidth, text = "Length (seconds):")
    label_songSamples = tk.Label(frame_songWindow, anchor='e', width = songDetailWidth, text = "Total Samples:")

    text_songNameChosen  = tk.Label(frame_songWindow, width = widgetWidth, anchor='w', text = "")
    text_songSampleRate  = tk.Label(frame_songWindow, width = widgetWidth, anchor='w', text = "")
    text_songBitRateType = tk.Label(frame_songWindow, width = widgetWidth, anchor='w', text = "")
    text_songLength      = tk.Label(frame_songWindow, width = widgetWidth, anchor='w', text = "")
    text_songSamples     = tk.Label(frame_songWindow, width = widgetWidth, anchor='w', text = "")

    #Assign Values from Song
    try:
        text_songNameChosen.config(text = song.inputFile)
        text_songLength.config(text = song.length)
        text_songSampleRate.config(text = song.sampleRate)
        text_songBitRateType.config(text = song.bitrateMode)
        text_songSamples.config(text = song.samples)
    except:
        fileNotSelected()


    #Assign to locations
    frame_songWindow.grid(row = 0, column= 0)

    label_songNameChosen.grid(row=1, column=0)
    label_songSampleRate.grid(row=2, column=0)
    label_songBitrateType.grid(row=3, column=0)
    label_songLength.grid(row=4, column=0)
    label_songSamples.grid(row=5, column=0)

    text_songNameChosen.grid(row=1, column=1)
    text_songSampleRate.grid(row=2, column=1)
    text_songBitRateType.grid(row=3, column=1)
    text_songLength.grid(row=4, column=1)
    text_songSamples.grid(row=5, column=1)
    

######Subcommands

# Clears active frame of all widgets
def clearWindow():

    for widget in frame.winfo_children():
        widget.destroy()    

#Opens a dialog box to state a file is either incorrect or has not been selected
def fileNotSelected():
    tk.messagebox.showinfo("", 'No File Selected')

#Open File selector to select music file, catches to fileNotSelected
def select_file(index, section):
    filetypes = ( ('MP3 Files', '*.mp3'),('All files', '*.*') )

    global indexStart

    try:
        filename = fd.askopenfilename(title='Open a file', initialdir='/', filetypes=filetypes)
    
        #showinfo(title='Selected File', message=filename)

        #Attempt to assign song data to labels
        testSong[index+indexStart] = debug.debugFileTest(filename,0)
        section.text_songNameChosen.config(text = testSong[index+indexStart].inputFile)
    except:
        fileNotSelected()

#Yeah
def close():
    if messagebox.askokcancel("Exit Application", "Close DDMod?"):
        root.destroy()
        sys.exit()
        
#increase indexStart for window selection
def incrementTen():
    global indexStart 
    indexStart += 10
    #print(indexStart)
    openSelectorWindow()

#decrease indexStart for window selection
def decrementTen():
    global indexStart 
    indexStart -= 10
    #print(indexStart)
    openSelectorWindow()




# create the root window
root = tk.Tk()
root.title('DDMOD')
root.resizable(False, False)
root.geometry('500x500')


##Create Frames
frame = tk.Frame(root)          # assign our base frame to the tkinter thing

##Widget Locations on the grid  
#Frames
frame.grid(row=0,column=0)



#Open main window
openMainWindow()

# run the application
root.protocol("WM_DELETE_WINDOW",close)
root.mainloop()
