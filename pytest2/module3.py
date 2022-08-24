

#We start parsing stuff here
def loadSongList():
    songFile = open('Song List.txt')

    fileBuffer = songFile.read()
    songFile.close()

    gameSong = fileBuffer.split(',\n')
    return gameSong

    
