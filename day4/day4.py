'''
        1.准备商品
        2.空的购物车
        3.钱包初始化金钱
        4.最后打印购物小条
    1.业务：
        看到商品：
            商品存在
                看金钱够：
                    成功加入购物车。
                    余额减去对应价格。
                不够：
                    穷鬼，去买其他商品。
            商品不存在：
                输入错误。
            输入Q或q，退出并结算。打印小条。
    任务：尽量多的添加商品
    任务：10个GIVENCHY8折优惠券，20个FENTY BEAUTY5折优惠券，免单一张优惠券，
    先整体打折8后在单独打折，在进入商城时，随机抽取优惠券，在最后结算使用改优惠券。
'''
#超市
import random
n=random.randint(1,3)
print(n)
b=0.8
c=0
if n==1:
    c=0.8
    print("GIVENCHY8折优惠券")
if n==2:
    c=0.5
    print("FENTY BEAUTY5折优惠券")
if n==3:
    c=0
    print("免单")

shop=[
    # 0     1
    ["MAC",170],#0
    ["YSL",335],#1
    ["CHANEL",350],#2
    ["GIVENCHY",500],#3
    ["ARMANI",310],#4
    ["FENTY BEAUTY",400],#5
    ["GUCCI",370],#6
    ["HERMES",525]#7
]
mycar=[]#购物车
money=3000#初始化钱包
cmoney=money
#               枚举
while True:
    for i in enumerate(shop):#列举商品
        print(i)
    o=input("请选择商品编号")#str  转换成int类型
    # 一个元素在某一个容器里面：
    if o.isdigit():#.isdigit判读字符串内是不是由数字组成
        o=int(o)#把str转换成int
        if o <len(shop):#判断输入的范围
            if money>shop[o][1]:#钱够不够
                mycar.append(shop[o])#加入购物车
                if n==3:
                    money=money-shop[o][1] * b * c
                    print("已加购，余额：",money)
                    c=1
                    continue
                if o==3:
                    money = money - shop[o][1] * b * c
                    print("已加购，余额：",money)
                    c=1
                    continue
                if o==5:
                    money = money - shop[o][1] * b * c
                    print("已加购，余额：", money)
                    c=1
                    continue
                else:
                    money = money - shop[o][1] * b
                    print("已加购，余额：", money)
                    continue
            else:print("穷鬼，gun")
        else:print("请输入正确的商品编号")
    elif o =="q" or o=="Q":#输入内容退出并打印小条
        cmoney=cmoney-money
        print("再见,以下是您购买的商品")
        for i in enumerate(mycar):
            print(i)
        print("共消费：",cmoney)
        break
    else:print("您输入的有误")