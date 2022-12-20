import binascii as bin

#### The hex converter

def convertHex(value):
    nug = hex(value)

   # buffer = nug.split('0x')
   # nug = buffer[1]

    print(nug)
    print(len(nug))

def loadSongList():
    songFile = open('bgm.stq', 'rb')
    
    fileBuffer = songFile.read()

    songFile.close()
   
    #gameSong = fileBuffer.split(',\n')
    #return gameSong

    #print(fileBuffer)
    #print(gameSong)

    test = "S"
    test = bin.hexlify(fileBuffer)
    print(test)
    




#convertHex(284544922)
loadSongList()