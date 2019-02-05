from zipfile import ZipFile
from threading import Thread
import os
import time
import resource


class ZipThread(Thread):
    def __init__(self, filename):
        Thread.__init__(self)
        self.filename = filename
        self.start_time = 0
        self.end_time = 0

    def run(self):
        self.start_time = time.time()
        print('Thread %s is zipping %s' % (self.filename.split('.')[0], self.filename))
        with ZipFile('%s.zip' % filename.split('.')[0], 'w') as archive:
            archive.write(filename)
        self.end_time = time.time()
        print('File %s zipped in %.5f seconds' % (self.filename, self.end_time - self.start_time))
        # TODO: Add Mem usage output. Not working example:
        # print('File %s zipped in %.5f seconds. MEM: %i'% (self.filename, self.end_time - self.start_time, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss))


if __name__ == "__main__":

    os.chdir("./data")
    for filename in ['%s.txt' % str(i) for i in range(1, 11)]:
        thread = ZipThread(filename)
        thread.start()
