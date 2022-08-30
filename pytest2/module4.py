

#### The hex converter

def convertHex(value):
    nug = hex(value)

    buffer = nug.split('0x')
    nug = buffer[1]

    print(nug)
    print(len(nug))

convertHex(28454492)