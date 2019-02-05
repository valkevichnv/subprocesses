import time
from threading import Thread
from threading import Event


class TimerThread(Thread):
    def __init__(self, event):
        Thread.__init__(self)
        self.stopped = event

    def run(self):
        print(time.ctime())
        while not self.stopped.wait(1):
            print(time.ctime())


stopFlag = Event()
thread = TimerThread(stopFlag)

thread.start()
while True:
    if input() == ' ':
        stopFlag.set()
        break
