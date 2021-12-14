class chef():
    name=""
    age=""

class cook(chef):
    def cooking(self,cai):
        print("炒菜")

class cook2(cook):
    def cooking(self,cai):
        super().cooking(cai)
        print("厨师：",self.name,",",self.age,"岁",cai)
c=cook2()
c.name="mikin"
c.age="45"
c.cooking("鱼香肉丝")

