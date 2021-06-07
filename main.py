from time import sleep, time, localtime
from playsound import playsound


class Broadcaster:
    def __init__(self):
        self.targetTime = 1654563600.0

    def getTimeDistance(self):
        nowTime = int(time())
        self.nowTime = localtime(nowTime)
        self.timeDistance = str(int((self.targetTime - nowTime) // (3600 * 24)))

    def cast(self):
        year = str(self.nowTime[0])
        mon = str(self.nowTime[1])
        day = str(self.nowTime[2])
        playsound("today.wma")
        self.readYear(year)
        playsound("year.wma")
        self.readNum(mon)
        playsound("mon.wma")
        self.readNum(day)
        playsound("day.wma")
        sleep(1)
        playsound("gaokao.wma")
        self.readNum(self.timeDistance)
        playsound("tian.wma")

    @staticmethod
    def readYear(year):
        for num in year:
            playsound(num + '.wma')

    @staticmethod
    def readNum(a):
        if len(a) == 1:
            playsound(a[0] + ".wma")
        elif len(a) == 2:
            if a[1] == "0":
                if a[0] != "1":
                    playsound(a[0] + ".wma")
                playsound("shi.wma")
            else:
                playsound(a[0] + ".wma")
                playsound("shi.wma")
                playsound(a[1] + "")
        else:
            playsound(a[0] + ".wma")
            playsound("bai.wma")
            if a[2] == "0":
                if a[1] != "1":
                    playsound(a[1] + ".wma")
                playsound("shi.wma")
            else:
                playsound(a[1] + ".wma")
                playsound("shi.wma")
                playsound(a[2] + ".wma")


if __name__ == "__main__":
    Gaokao = Broadcaster()
    Gaokao.getTimeDistance()
    Gaokao.cast()
