from ast import Str
import tkinter as tk
from tkinter.constants import NONE
import tkinter.font as tkFont
import sys

from tkinter import StringVar, Toplevel, ttk
from tkinter import filedialog as fd
from tkinter import messagebox

from tkinter.messagebox import showinfo
from typing import Counter, Text

import module2 as debug


#Set width for widgets that require it
widgetWidth = 30

#Initialize array for the Selecting container
selectIndex = [None]
indexSize = 5

#Initialize array container to hold songs 
testSong = [None] * 10

#Initialize empty container for windows
activeWindow = None

def select_file(index, section):
    filetypes = ( ('MP3 Files', '*.mp3'),('All files', '*.*') )
    
    try:
        filename = fd.askopenfilename(title='Open a file', initialdir='/', filetypes=filetypes)
    
        #showinfo(title='Selected File', message=filename)

        #Attempt to assign song data to labels
        testSong[index] = debug.debugFileTest(filename,0)
        section.text_songNameChosen.config(text = testSong[index].inputFile)
    except:
        fileNotSelected()

def close():
    if messagebox.askokcancel("Exit Application", "Close DDMod?"):
        root.destroy()
        sys.exit()
        
def openSongDetails(song):
    songDetailsWindow = Toplevel(root)
    songDetailsWindow.title('Song Details')
    songDetailsWindow.geometry('400x400')
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

class window_songSelector:

    def __init__(self,frame):
       populateSelector(indexSize, selectIndex)

       self.button_Return = ttk.Button(frame, width=10, text='< back' ,command=lambda:openMainWindow())

       self.button_Return.grid(row = indexSize, column = 0)

class component_songSelector:

    # I create the song selectors as a class so that I can instantiate it several times.
    # More work initially but scales.

    def __init__(self, frame, count):
        ##Create Widgets
        #open button   


        
        self.label_songName        = tk.Label(frame, text = "Selected song")
        self.text_songNameChosen  = tk.Label(frame, width = widgetWidth, anchor='w', text = "")

        # Using a lambda to prevent the function from being called prematurely
        self.button_openFile = ttk.Button(frame,text='...', width=3, command= lambda: select_file(count, self))
        self.button_openWindow = ttk.Button(frame,text='?', width=3, command= lambda: openSongDetails(testSong[count])) 



        # Widget placement

        self.label_songName.grid(row=count, column=0)
        self.text_songNameChosen.grid(row=count, column=1)
        self.button_openFile.grid(row=count, column=2)
        self.button_openWindow.grid(row=count,column=3)

def populateSelector(count, container):

  index = 0
  container = [None] * count
  while (index<=count-1):  
        container[index] = component_songSelector(frame, index)
        if testSong[index] != None:
            container[index].text_songNameChosen.config(text=testSong[index].inputFile)
        index = index+1
  print(container)
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



def openSelectorWindow():  
    clearWindow()
    activeWindow = window_songSelector(frame)
    #activeWindow = populateSelector(5)

def openMainWindow():
    clearWindow()
    activeWindow = window_Main(frame)



#Subcommands
def clearWindow():

    for widget in frame.winfo_children():
        widget.destroy()    

def fileNotSelected():
    tk.messagebox.showinfo("", 'No File Selected')

# create the root window
root = tk.Tk()
root.title('DDMOD')
root.resizable(False, False)
root.geometry('400x400')


##Create Frames
frame = tk.Frame(root)          # assign our base frame to the tkinter thing
#subFrame = tk.Frame(root)      # assign our subframe to the base frame

##Widget Locations on the grid  
#Frames
frame.grid(row=0,column=0)



#Open main window
openMainWindow()

# run the application
root.protocol("WM_DELETE_WINDOW",close)
root.mainloop()
