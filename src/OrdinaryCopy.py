from timeit import default_timer as timer

from Copy import Copy


class OrdinaryCopy(Copy):
    def runCopy(self):
        start = timer()
        for fileName in self.fileNames:
            self.copyTask(fileName)
        end = timer()
        print('{} seconds'.format(end - start))


runner = OrdinaryCopy()
runner.runCopy()
