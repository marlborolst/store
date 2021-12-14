#水杯
#属性:高度，容积，颜色，材质
#功能:能存放液体
class cup:
    high = ""
    color = ""
    v = ""
    tex = ""
    fun = ""

    def gd(self):
        print("水杯高为:",self.high)

    def ys(self):
        print("水杯颜色为:",self.color)

    def rj(self):
        print("水杯容积为:",self.v)

    def cz(self):
        print("水杯材质为:",self.tex)

    def gn(self):
        print("水杯的功能为:",self.fun)

c=cup()

c.high="18cm"
c.v="555ml"
c.color="pink(*╹▽╹*)"
c.tex="gold"
c.fun="存放液体"

c.gd()
c.ys()
c.rj()
c.cz()
c.gn()

#笔记本电脑
#屏幕大小，价格，cpu型号，内存大小，待机时长，
#行为（打字，打游戏，看视频）
class computer:
    name = ""
    size = ""
    money = ""
    cpu = ""
    internal = ""
    time = ""

    def type(self,type):
        print(self.name,"可以",type)

    def game(self,game):
        print(self.name,"可以",game)

    def video(self,video):
        print(self.name,"可以",video)

    def show(self):
        print("电脑：",self.name,"大小：",self.size,"价格：",self.money,"cpu:",self.cpu,"内存：",self.internal,"待机时长：",self.time)

c = computer()

c.name = "dell"
c.size = "20*30"
c.money = "7999"
c.cpu = " i5-8250U"
c.internal = "8.00 GB"
c.time = "48h"

c.show()
c.type("打字")
c.game("打游戏")
c.video("看视频")