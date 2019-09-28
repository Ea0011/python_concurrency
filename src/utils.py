from setup import SOURCE_DIR, DEST_DIR
from shutil import copy
from os import listdir


def copyFile(sourceFileName):
    copy(
        getSourceFilePath(sourceFileName),
        getDestinationFilePath(sourceFileName)
    )


def getSourceFilePath(index):
    return '{}/{}'.format(SOURCE_DIR, index)


def getDestinationFilePath(index):
    return '{}/{}'.format(DEST_DIR, index)


def getSourceFileNames():
    files = [f for f in listdir(SOURCE_DIR)]
    return files


print(len(getSourceFileNames()))
