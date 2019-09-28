from abc import abstractclassmethod

from utils import getSourceFileNames, copyFile


class Copy:
    def __init__(self):
        self.fileNames = getSourceFileNames()

    def copyTask(self, fileName):
        copyFile(fileName)

    @abstractclassmethod
    def runCopy(self):
        pass
