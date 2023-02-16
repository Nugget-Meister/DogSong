import binascii as bin

#### The hex converter

def convertHex(value):
    nug = hex(value)

   # buffer = nug.split('0x')
   # nug = buffer[1]

    print(nug)
    print(len(nug))

def loadSongList():
    #songFile = open('bgm.stq', 'rb')
    songFile = open('bgm.stq', 'rb')

    fileBuffer = songFile.read()

    songFile.close()
   
    #gameSong = fileBuffer.split(',\n')
    #return gameSong

    #print(fileBuffer)
    #print(gameSong)

    #test = fileBuffer
    test =  [str(bin.hexlify(fileBuffer))]

    #Create beginning of chunker into usable format
    testB = list()
    chunkSize = 8
    

    for i in range(2, len(test[0])-1, chunkSize):
        testB.append(test[0][i:i+chunkSize])

    print(testB)
    #print(test)
   # print(len(test[0]))
    




#convertHex(284544922)
loadSongList()