# import time module
import time


class StopWatch:
    def __init__(self):
        # class variables
        self.__startTime = 0
        self.__endTime = 0

    def getStartTime():
        """return the starting time of the stop watch"""
        return self.__startTime

    def getEndTime():
        """return the end time of the stop watch"""
        return self.__endTime

    def start(self):
        """start the stop watch"""
        self.__startTime = time.perf_counter()
        print("Stop watch started")

    def stop(self):
        """stop the stop watch"""
        self.__endTime = time.perf_counter()
        print("Stop watch stopped")

    def getElapsedTime(self):
        """print how much time has elapsed between the start and stop times of the 
  stop watch"""
        print(f"{self.__endTime - self.__startTime} seconds elapsed")


# initiate stop watch instance
x = StopWatch()
# start the stop watch
x.start()
# not sure what you meant by add all numbers between 1 and 1,000,000, so assuming you meant this:
for i in range(1000000):
    i += i
# stop the stop watch
x.stop()
# get how much time has elapsed(how long our code took to execute)
x.getElapsedTime()
