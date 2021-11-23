'''
需求：
1、猜的数字是系统产生的，不是自己定义的
2、键盘输入的   操作完填入：input（“提示”）
3、判断			操作完填入：if判断条件 elif 判断条件。。。。。。Else
4、循环			操作完填入：while 条件循环
任务：如果键盘输入大于随机数弹出友好提示信息“猜大了”，猜小了
起始金额  5000 才对一次给300 猜错扣除100 猜错15次结束
'''
money=5000
tmoney=300
fmoney=100
i=0
import random
Ran = random.randint(1, 20)
while True:
            num = input("请输入一个数字")
            num = int(num)
            if num == Ran:
                money=money+tmoney
                print("猜对了")
            else:
                if num>Ran:
                    print("猜大了")
                else:
                    print("猜小了")
                money=money-fmoney
            print("money=",money)
            i=i+1

            if i==15:
                break