#CRAPS又称花旗骰，是美国拉斯维加斯非常受欢迎的一种的桌上赌博游戏。
# 该游戏使用两粒骰子，玩家通过摇两粒骰子获得点数进行游戏。简单的规则是：
import random
money=1000
while True:
    i = input("请下注：")
    i = int(i)
    while True:
        if i>money:
            print("余额不足")
            i = input("请下注：")
            i = int(i)
        else:
            break
    craps1=random.randint(1,6)
    print("玩家摇出了",craps1,"点")
    craps2=random.randint(1,6)
    print("玩家摇出了", craps2, "点")
    craps3=craps1+craps2
# 玩家第一次摇骰子如果摇出了7点或11点，玩家胜；
    while True:
            if craps3==7:
                print("玩家胜")
                money=money+i
                print("你的总资产为：",money)
                break
            else:
                if craps3==11:
                    print("玩家胜")
                    money = money + i
                    print("你的总资产为：",money)
                    break
# 玩家第一次如果摇出2点、3点或12点，庄家胜；
                else:
                    if craps3==2:
                        print("庄家胜")
                        money = money - i
                        print("你的总资产为：", money)
                        break
                    else:
                        if craps3 == 3:
                            print("庄家胜")
                            money = money - i
                            print("你的总资产为：", money)
                            break
                        else:
                            if craps3 == 12:
                                print("庄家胜")
                                money = money - i
                                print("你的总资产为：", money)
                                break
# 其他点数玩家继续摇骰子，如果玩家摇出了7点，庄家胜；
                            else:
                                craps1 = random.randint(1, 6)
                                print("玩家摇出了", craps1, "点")
                                craps2 = random.randint(1, 6)
                                print("玩家摇出了", craps2, "点")
                                craps4 = craps1 + craps2
                                if craps4 == 7:
                                    print("庄家胜")
                                    money = money - i
                                    print("你的总资产为：", money)
                                    break
# 如果玩家摇出了第一次摇的点数，玩家胜；
                                else:
                                    if craps4 == craps3:
                                        print("玩家胜")
                                        money=money+i
                                        print("你的总资产为：", money)
                                        break
# 其他点数，玩家继续要骰子，直到分出胜负。
# 假设我有1000元，直到我输光游戏结束
    if money<=0:
        print("你已破产，游戏结束。")
        break
    else:
        continue
