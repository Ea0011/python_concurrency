from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, wait
from timeit import default_timer as timer

from setup import NUM_OF_WORKERS
from Copy import Copy


class ConcurrentCopyWithExecutor(Copy):
    def __init__(self, executorClass):
        Copy.__init__(self)
        self.executorClass = executorClass

    def runCopy(self):
        start = timer()
        with self.executorClass(max_workers=NUM_OF_WORKERS) as copyExecutor:
            copyResults = [
                copyExecutor.submit(self.copyTask, fileName) for fileName in self.fileNames
            ]
            wait(copyResults)
        end = timer()
        print('{} seconds {}'.format((end - start), self.executorClass.__name__))


threadRunner = ConcurrentCopyWithExecutor(executorClass=ThreadPoolExecutor)
threadRunner.runCopy()

processRunner = ConcurrentCopyWithExecutor(executorClass=ProcessPoolExecutor)
processRunner.runCopy()
