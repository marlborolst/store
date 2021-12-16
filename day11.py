from threading import Thread
import time

box=0
class cook(Thread):
    chefname=""
    work=0
    workmoney=0
    def run(self) -> None:
        global box
        while True:

            if box == 500:
                print("篮子满了，有", box, "个蛋挞")
                time.sleep(3)

            if box < 500:
                box = box + 1
                self.work = self.work + 1
                self.workmoney = self.workmoney + 1.5
                print(self.chefname, "做了1个蛋挞", "篮子里有", box, "个蛋挞")
                print()
            else:
                print(self.chefname, "总共做了", self.work, "个蛋挞，赚了", self.workmoney, "元")
                print()
                break

class costmer(Thread):
    name = ""
    money=30000
    zmoney=0
    count=0

    def run(self) -> None:
        global box

        while True:
            if box >0 :
                if self.money > 3:
                    self.count = self.count + 1
                    self.money = self.money - 3

                    box = box - 1
                    print(self.name,"抢了",self.count,"个蛋挞","花了",3*self.count,"元",end="")

                else:
                    print()
                    print(self.name,"没钱了！！！！！！！！！！！！！！！！！！！！！！！！！")
                    print()
                    break


cc1=cook()
cc2=cook()
cc3=cook()

cc1.chefname="厨师A"
cc2.chefname="厨师B"
cc3.chefname="厨师C"

cc1.start()
cc2.start()
cc3.start()

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


