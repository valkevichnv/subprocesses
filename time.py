import time
from threading import Thread
from threading import Event


class TimerThread(Thread):
    def __init__(self, event):
        Thread.__init__(self)
        self.stopped = event

    def run(self):
        print(time.ctime())
        while not self.stopped.wait(30):
            print(time.ctime())


stopFlag = Event()
thread = TimerThread(stopFlag)

thread.start()
if input() == ' ': stopFlag.set()
