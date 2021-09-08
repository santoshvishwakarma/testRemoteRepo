import datetime
import time

startHour = 0;
endHour = 0;


def checkTimeLog(timelog):
    try:
        assert len(list(timelog)) > 1
        getEntries(timelog)
    except AssertionError:
        print("Absent marked. time not logged properly.")


def getEntries(timelog):
    try:
        startHour = time.strptime(timelog.__getitem__(0)[6:8], '%H').tm_hour
        endHour = time.strptime(timelog.__getitem__(len(timelog) - 1)[6:8], '%H').tm_hour
        print(("Absent", "Present")[endHour - startHour > 8])
    except:
        print("Invalid timelog entry.")


def unitTests():
    checkTimeLog(["X4431-0900", "X4431-1800"])
    checkTimeLog(["X4431-0900", "X4431-1000", "X4431-1130", "X4431-1300", "X4431-1600"])
    checkTimeLog(["X4431-0900"])
    checkTimeLog([])
    checkTimeLog(["ABC", "XYZ"])


unitTests()
