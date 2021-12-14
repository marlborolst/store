import time
class oldphone():
    pinpai=""
    mynumber=""
    def call(self,number):
        print(self.mynumber,"正在给",number,"打电话...")
        for i in range(4):
            print(".",end="")
            time.sleep(1)

class newphone(oldphone):
    def call(self,number):
        print("语音拨号中...")
        super().call(number)
    def jieshao(self):
        print("品牌为：",self.pinpai,"的手机很好用...")

phone=newphone()
phone.mynumber="18340357322"
phone.pinpai="oppo"
phone.call("6194276")
phone.jieshao()