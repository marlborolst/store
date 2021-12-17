from threading import Thread
import time
import threading
import sys

box=0
start=time.time()

class cook(Thread):
    m1=threading.Lock()
    chefname=""
    work=0
    workmoney=0
    def run(self) -> None:
        global box
        while True:
            self.m1.acquire()
            end = time.time()
            if end - start >= 10:
                print("本店只营业3分钟！不卖了！！！！！！！！！！！！！！！！！！！！！！！！")
                sys.exit()
            if box == 500:
                print("篮子满了，请3秒后再做！")
                time.sleep(3)
            if box < 500:
                box = box + 1
                self.work = self.work + 1
                self.workmoney = self.workmoney + 1.5
                print(self.chefname, "----------做了1个蛋挞", "篮子里有", box, "个蛋挞", "总共做了", self.work, "个蛋挞，赚了", self.workmoney, "元")
                self.m1.release()

class costmer(Thread):
    m2=threading.Lock()
    name = ""
    money=30000
    count=0
    def run(self) -> None:
        global box
        while True:
            self.m2.acquire()
            end = time.time()
            if end - start >= 10:
                sys.exit()
            if box == 0:
                print(self.name,"蛋挞不足请等待3秒")
                time.sleep(3)
            if box >0 :
                if self.money >= 3:
                    self.count = self.count + 1
                    self.money = self.money - 3
                    box = box - 1
                    print(self.name,"..........抢了",self.count,"个蛋挞","花了",3*self.count,"元","篮子里还剩",box,"个蛋挞")
                    time.sleep(0.1)
            self.m2.release()
cc1=cook()
cc2=cook()
cc3=cook()

cc1.chefname="厨师A"
cc2.chefname="厨师B"
cc3.chefname="厨师C"

c1=costmer()
c2=costmer()
c3=costmer()
c4=costmer()
c5=costmer()
c6=costmer()

c1.name="顾客1"
c2.name="顾客2"
c3.name="顾客3"
c4.name="顾客4"
c5.name="顾客5"
c6.name="顾客6"

c1.start()
c2.start()
c3.start()
c4.start()
c5.start()
c6.start()

cc1.start()
cc2.start()
cc3.start()
