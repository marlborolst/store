import random
print("===============")
print("| 皮克斯のBANK |")
print("===============")
print("|   1、开户    |")
print("|   2、存钱    |")
print("|   3、取钱    |")
print("|   4、转账    |")
print("|   5、查询    |")
print("===============")
#定义一个空字典,当作数据库
bank={}
bank_name="中国工商银行"
#定义方法————用来添加用户的
def useradd():
    account=random.randint(10000000,99999999)#随机生成8位数账号
    username=input("请输入您的姓名")
    password=input("请输入您的密码")
    country=input("请输入您的国家")#\t表示一个tab
    province=input("请输入您的省份")
    street=input("请输入您的街道")
    door=input("请输入您的门牌")
    gift=bankadd(account,username,password,country,province,street,door)#位置对应
    if gift =="1" :
        print("开户成功,以下是您的详细信息")
        #模板
        info='''
                --------工商银行-------
                    1、账号：%s
                    2、姓名：%s
                    3、密码：******
                    4、国家：%s
                    5、省份：%s
                    6、街道：%s
                    7、门牌：%s
                    8、余额：%s
        '''
        print(info % (account,username,country,province,street,door,bank[username]["money"]))#打印模板
    elif gift =="2":#用户已存在
        print("请使用其他用户")
    elif gift =="3":#银行能存储100用户的库(字典)
        print("数据库已满")
#往字典里面存数据
def bankadd(account,username,password,country,province,street,door):
    if username in bank:#  姓名已经在bank的键里
        return "2"
    elif len(bank)>=100:
        return "3"
# 字典 以[username]作为建（它的值又是一个字典）,往bank里添加
    bank[username]={
        "account":account,#从useradd的account获取的随机数
        "password":password,
        "country":country,
        "province":province,
        "street":street,
        "door":door,
        "bank_name":bank_name,
        "money":0
    }
    return "1"
while True:
    box=input("请输入编号:")
    if box=="1":
        print("1、开户")
        useradd()
    elif box=="2":
        print("2、存钱")
    elif box=="3":
        print("3、取钱")
    elif box=="4":
        print("4、转账")
    elif box=="5":
        print("5、查询")