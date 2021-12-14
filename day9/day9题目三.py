#人类：
'''
属性:
姓名，性别，年龄，所拥有的手机剩余话费，手机品牌，手机电池容量，
手机屏幕大小，手机最大待机时长，所拥有的积分。'''
#功能：
#发短信（要求参数传入短信内容）。
#打电话（要求传入要打的电话号码和要打的时间长度。
#程序里判断号码是否为空或者本人的话费是否小于1元，
#若为空或者小于1元则报相对应的错误信息，否则的话拨通。
#结束后，按照时间长度扣费并返回扣费
#（0~10分钟：1元/钟、15个积分/钟，10~20分钟：0.8元/钟、39个积分/钟，
#其他：0.65元/钟、48个积分/钟））
class person:
    __name=""
    __sxe=""
    __age=0
    __logo=""
    __v=0
    __size=0
    __djtime=0
    __point=0

    def setname(self,name):
        if name == "":
            print("姓名不能为空")
        else:
            self.__name = name
    def getUsername(self):
        return self.__name

    def setsex(self,sex):
        if sex != "男" and sex != "女":
            print("性别非法")
        else:
            self.__sex = sex
    def getSex(self):
        return self.__sex

    def setAge(self,age):
        if age > 120  or age < 0:
            print("年龄非法")
        else:
            self.__age  = age
    def getAge(self):
        return  self.__age

    def setlogo(self,logo):
        self.__logo=logo
    def getlogo(self):
        return self.__logo

    def setv(self,v):
        if v <0:
            print("电池容量非法")
        else:
            self.__v=v
    def getv(self):
        return self.__v

    def setsize(self,size):
        if size <0:
            print("屏幕大小非法")
        else:
            self.__size=size
    def getsize(self):
        return self.__size

    def setdjtime(self,djtime):
        if djtime <0:
            print("待机时长非法")
        else:
            self.__djtime=djtime
    def getdjtime(self):
        return self.__djtime

    def setmoney(self,money):
        self.__money=money
    def getmoney(self):
        return self.__money

    def setpoint(self,point):
        if point <0:
            print("积分不能为负")
        else:
            self.__point=point
    def getpoint(self):
        return self.__point

    def massage(self,massage):
        print("正在发送短信：",massage)
        print()
        print("===========================")
        print()
    def setphone(self,num,time):
        if num == "" :
            print("号码为空")
        elif self.__money<1:
            print("话费不足")
        else:
            print("姓名",self.__name)
            print("性别",self.__sex)
            print("年龄",self.__age)
            print("手机品牌",self.__logo)
            print("电池容量",self.__v)
            print("手机屏幕大小",self.__size)
            print("待机时长",self.__djtime,"h")

            print("拨通号码：", num)
            print("通话时间：", time, "min")
            print("话费余额：", self.__money, "元")
            print("现有积分：", self.__point)
            if 0<time<10:
                self.__money=self.__money-1*time
                self.__point=self.__point+15*time
            elif 10<time<20:
                self.__money=self.__money-0.8*time
                self.__point=self.__point+39*time
            else:
                self.__money = self.__money - 0.65 * time
                self.__point = self.__point + 48 * time
            print("==========开始通话==========")
            print()
            print()
            print()
            print("==========通话结束==========")
            print("通话时间：", time, "min")
            print("话费余额：", self.__money, "元")
            print("剩余积分：", self.__point)

    def getphone(self):
        return self.__money
p=person()

p.setname("molly")
p.setsex("女")
p.setAge(16)
p.setlogo("oppo")
p.setsize(32)
p.setv(900)
p.setmoney(100)
p.setpoint(0)
p.setdjtime(24)

p.massage("misss u")
p.setphone("0429-6194276",60)
#             num,  time,money,point)
