import os

def rename():
    fileList = os.listdir("/home/mike/UdacityPy/pictures")

    print fileList
    savedPath = os.getcwd()
    os.chdir("/home/mike/UdacityPy/pictures")
    for fileName in fileList:
        os.rename(fileName, fileName.translate(None,"1234567890") )
    os.chdir(savedPath)


rename()
