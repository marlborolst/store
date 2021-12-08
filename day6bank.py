print("===============")
print("|  皮克斯の银行 |")
print("===============")
print("|   1、开户    |")
print("|   2、存钱    |")
print("|   3、取钱    |")
print("|   4、转账    |")
print("|   5、查询    |")
print("|   6、Bey!   |")
print("===============")
import random
bank={}#定义一个空字典,当作数据库
bank_name="皮克斯の银行"
#定义方法————用来添加用户的
def useradd():
    account=random.randint(10000000,99999999)#随机生成8位数账号
    username=input("请输入您的姓名")
    password=input("请输入您的密码")
    country=input("请输入您的国家")#\t表示一个tab
    province=input("请输入您的省份")
    street=input("请输入您的街道")
    door=input("请输入您的门牌")

    i=bankadd(account,username,password,country,province,street,door)#位置对应bankadd()
    #返回值：整型值（1：成功，2：用户已存在，3：用户库已满）
    if i =="1" :
        print("开户成功,以下是您的详细信息")
        #模板
        info='''
                --------皮克斯の银行-------
                        1、账号：%s
                        2、姓名：%s
                        3、密码：******
                        4、国家：%s
                        5、省份：%s
                        6、街道：%s
                        7、门牌：%s
                        8、余额：%s          '''
        print(info % (account,username,country,province,street,door,bank[username]["money"]))#打印模板
    elif i =="2":
        print("用户已存在")
    elif i =="3":#银行能存储100用户的库(字典)
        print("数据库已满")


#往字典里面存数据 传入参数：用户的所有信息。
def bankadd(account,username,password,country,province,street,door):
    if username not in bank:
    # 字典 以[username]作为建（它的值又是一个字典）,往bank里添加
    #       键                   值
    #                       键       值
        bank[username] = {"account": account,  # 从useradd()的account获取的随机数
                          "password": password,
                          "country": country,
                          "province": province,
                          "street": street,
                          "door": door,
                          "bank_name": bank_name,
                          "money": 0}
        return "1"  # 添加成功
    if username in bank:#  判断username已经在bank的键里
        return "2"
    elif len(bank)>=100:
        return "3"



#定义方法————用来存钱   （传入值：用户的账号、存取的金额。返回值：布尔类型值）
#业务逻辑：
#先根据传入的账号信息查询用户库里是否有该用户。若没有则返回False
#若有，则将该用户的金额存进去。
def cqadd():
    username=input("输入用户名")
    money=int(input("输入金额"))

    A=saveadd(username, money)

    if A==True:
        print("存款成功,余额为：", bank[username]["money"])
    else:
        print("不存在")

def saveadd(username,money):#传入值：用户的账号、存取的金额
    if username not in bank:
        return False
    else:
        bank[username]["money"]=bank[username]["money"]+money
        return True




#定义方法————用来取钱   （传入值：用户的账号，用户密码，取钱金额。
# 返回值：整型值（0：正常，1：账号不存在，2：密码不对，3：钱不够））
#a)业务逻辑：
#先根据账号信息来查询该用户是否存在，若不存在，则返回代号1，
#若存在，则继续判断密码是否正确，若不正确，则返回代号2。
#若账号密码都正确，则继续判断当前用户的金额是否满足要取出的钱，若不满足，则返回代号3，
#若满足，则将该用户的金额减去。
def qqadd():
    username=input("输入用户名")
    password=input("输入密码")
    money=int(input("输入金额"))
    g=withdraw_money(username,password,money)
    if g=="1":
        print("不存在")
    elif g =="2":
        print("密码错误")
    elif g=="3":
        print("余额不足")

def withdraw_money(username,password,money):#传入值：用户的账号，用户密码，取钱金额。
    if username not in bank:
        return "1"
    elif password != bank[username]["password"]:
        return "2"
    elif money > bank[username]['money']:
        return "3"
    else:
        bank[username]['money'] = bank[username]['money'] - money
        print("取款成功：余额:", bank[username]['money'])



#定义方法————用来转账（传入值：转出的账号，转入的账号，转出账号的密码，转出的金额。
# 返回值：0：正常，1：账号不对，2密码不对，3钱不够）
#a)业务逻辑：
#先查询用户库是否存在转出和转入的账号，若不存在则返回代号,1，
#若账号都存在则继续判断转出账号的密码是否正确，若不正确，则返回2，
#若正确则继续判断要转出的金额是否足够，若不够则返回3，
#否则正常转出，转出的账号用户金额要相对应的减少，转入的金额相对应的增加。
def zzadd():
    username1 = input("输入转入用户")
    username2 = input("输入转出用户")
    password = input("输入密码")
    money = int(input("输入金额"))
    c=move_money(username1, username2, password, money)
    if c == 1:
        print("账号错误")
    elif c == 2:
        print("密码错误")
    elif c == 3:
        print("余额不足")

def move_money(username1, username2, password, money):
    if username1 not in bank:
        return 1
    elif username2 not in bank:
        return 1
    elif password != bank[username2]["password"]:
        return 2
    elif money > bank[username2]['money']:
        return 3
    else:
        bank[username2]['money'] = bank[username2]['money'] - money
        bank[username1]['money'] = bank[username1]['money'] +money
        print("转账成功：余额:", bank[username2]['money'])
        return 0



#定义方法————用来查询账户（传入值：账号，账号密码，返回值：空）
#a)业务逻辑：
#先根据账号判断用户库是否存在该用户，若不存在则打印提示信息：该用户不存在。
#否则继续判断密码是否正确。若不正确则打印相对应的错误信息。
#若账号和密码都正确，则将该用户的信息都打印出来，
#比如：当前账号：xxxx,密码:xxxxxx,余额：xxxx元，用户居住地址：xxxxxxxxxxxxx，当前账户的开户行：xxxxxxxxxx.
def cxadd():
    username = input("输入账号")
    password = input("输入密码")
    findadd(username,password)
    info = '''
                            --------皮克斯の银行-------
                                    1、账号：%s                                    
                                    2、密码：%s
                                    3、余额：%s 元
                                    4、用户居住地址：国家：%s 省份：%s 街道：%s 门牌：%s
                                    5、当前账户的开户行：%s
                                             '''
    print(info % (bank[username]["account"], bank[username]["password"], bank[username]["money"],bank[username]["country"],
                  bank[username]["province"],bank[username]["street"],bank[username]["door"],bank_name
                  ))


def findadd(username,password):
    if username not in bank:
        print("该用户不存在")
    elif password != bank[username]["password"]:
        print("密码错误")
    else:
        return




while True:
    box=input("请输入编号:")
    if box=="1":
        print("1、开户")
        useradd()
    elif box=="2":
        print("2、存钱")
        cqadd()
    elif box=="3":
        print("3、取钱")
        qqadd()
    elif box=="4":
        print("4、转账")
        zzadd()
    elif box=="5":
        print("5、查询")
        cxadd()
    elif box=="6":
        print("6、Bey!")
        break
