import sys
import time


class TimeoutTest:

    def __init__(self, timeout):
        self.timeout = int(timeout)

    @staticmethod
    def current_time():
        print("The current time is %s" % (time.strftime("%Y-%m-%d %H:%M:%S")))

    def sleep(self):
        self.current_time()
        sleepTime = self.timeout + 60
        print("Start to sleep ... ")
        time.sleep(sleepTime)
        self.current_time()
       


if __name__ == '__main__':
    timeout = sys.argv[1]
    TimeoutTest(timeout).sleep()