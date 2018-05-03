# sImg Main Script

import easygui as eg
import sykesrle as rle
from PIL import Image as image
from os import remove

quitCall = False
while not quitCall:

    mainOption = eg.indexbox("Select an action...", "sImg - Main Menu", ["Quit","Encode", "Decode"])

    if mainOption == 0:

        quitCall = True

    elif mainOption == 1:

        actuallyFile = True
        inFile = str(eg.fileopenbox("Select an input file...", "sImg - Encode - Input FIle", "*.bmp", "Bitmaps|*.bmp"))
        if inFile == "None":
            actuallyFile = False
        else:
            outFile = str(eg.filesavebox("Select an output file...", "sImg - Encode - Output File", "*.simg", "sImgs|*.simg"))
            if outFile == "None":
                actuallyFile = False

        if actuallyFile:

            eg.msgbox("This may take some time, please wait.", "sImg - Encode - Message")

            inImage = image.open(inFile)
            inPix = inImage.load()
            width, height = inImage.size

            outData = ""
            for i in range(0, height):
                lineData = ""
                for j in range(0, width):
                    currentPixel = inPix[i, j]
                    if i == height and j == width:
                        trailer = "@"
                    elif not j == width:
                        trailer = "~"
                    lineData = "{0}{1}{2}".format(lineData, currentPixel, trailer)
                outData = "{0}{1}".format(outData, lineData)

            outOpen = open(outFile, "w")
            deleteOK = True
            try:
                remove(outFile)
            except:
                pass
            try:
                outOpen.write(outData)
            except:
                pass
            eg.msgbox("Finished encoding.", "sImg - Encode - Complete")

    elif mainOption == 2:

        actuallyFile = True
        inFile = str(eg.fileopenbox("Select an input file...", "sImg - Decode - Input FIle", "*.simg", "sImgs|*.simg"))
        if inFile == "None":
            actuallyFile = False
        else:
            outFile = str(eg.filesavebox("Select an output file...", "sImg - Decode - Output File", "*.bmp", "Bitmaps|*.bmp"))
            if outFile == "None":
                actuallyFile = False

        if actuallyFile:

            eg.msgbox("This may take some time, please wait.", "sImg - Decode - Message")

            inOpen = open(inFile)
            inData = inOpen.read()
            inLines = inData.split("@")

            width = len(inLines[0].split("~"))
            height = len(inLines)
            outImage = image.new("RGB", (width, height))
            outPixels = outImage.load()

            for ix, i in enumerate(inLines):
                inCurrent = i.split("~")
                for jx, j in enumerate(inCurrent):
                    outPixels[ix,jx] = tuple(j)

            outImage.save(outImage)

            eg.msgbox("Finished Decoding.", "sImg - Decode - Complete")