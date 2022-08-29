import tkinter as tk
from mutagen import *
import os

# The song converter, also loads song information/metadata

# By making the values in a class I can instantiate songs with values.


class songDef:
    def __init__(self, inputFile, length, sampleRate, bitrateMode, samples):
        self.inputFile = inputFile
        self.length = length
        self.sampleRate = sampleRate
        self.bitrateMode = bitrateMode
        self.samples = samples
        
# I can then return all the required information as a package/class

def debugFileTest(inputFilePath, verbose):  
   
    
    # Store the filepath as a file for mutagen so we can pull information later
    # Added Mutagen for Clarity
        inputFileMutagen = File(inputFilePath)
       
        # Shorthand Variable
        length=float(inputFileMutagen.info.length)
        sampleRate=float(inputFileMutagen.info.sample_rate)
        bitrateMode=(inputFileMutagen.info.bitrate_mode)
   
        # Calculate length at constant bit rate. Song may be VBR. if VBR this is inaccurate.

        samples = float(inputFileMutagen.info.length * inputFileMutagen.info.sample_rate)

        #Instantiate Class with song data // Uses InputFilePath from (fd)

        songList = songDef(inputFilePath,length,sampleRate,bitrateMode,samples)
    
        ## Get file information

        ##inputFile = File("C:\\ddmod\\mgstheme.mp3")
        # outputFile = File(outputfilePath)

        #This is just to test if the file/commands are working
        if (verbose == 1):
            print(length)                              # length in seconds
            print(sampleRate)                          # sample rate
            print(bitrateMode)                         # check if Variable or Constant Bit rate
            print(inputFileMutagen.info.pprint())      # print other detail
            print(samples)
            print()

        return songList

def convertOGG(inputFilePath, outputFilePath):
 
    ##################
    #
    ## Command to automate. example
    #
    # ffmpeg -i "C:/ddmod/mgstheme.mp3" -vn -ar 48000 "C:/ddmod/mgstheme.ogg"
    #
    #################


    convert = "cmd /k ffmpeg -i \"" + inputFilePath + "\" " + "-vn -ar 48000 \"" + outputFilePath + "\""
    print(convert)
    os.system(convert)

    ## launch ffmpeg
    ## os.system('cmd /k ffmpeg -i "C:\\ddmod\\mgstheme.mp3" -vn -ar 48000 "C:\\ddmod\\mgstheme.ogg" ')

