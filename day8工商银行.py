# author:jason
import random

from DBUtils import  update
from DBUtils import select
#银行库
bank = {}
bank_name = "中国工商银行昌平支行"
bank_choice = {"1":"开户","2":"存钱","3":"取钱","4":"转账","5":"查询","6":"Bye"}  # 银行业务选项
# 开户成功的信息模板
myinfo='''
    \033[0;32;40m
    ------------账户信息------------
    账号：{account}
    姓名：{username}
    密码：{password}
    地址：
        国家：{country}
        省份：{province}
        街道：{street}
        门牌号：{door}
    账户余额：{money}
    注册银行名：{bank_name}
    -------------------------------
    \033[0m
'''
# 欢迎模板
welcome = '''
***********************************
*      中国工商银行账户管理系统       *
***********************************
*               选项              *
'''
welcome_item = '''*              {0}.{1}             *'''

def print_welcome():
    print(welcome,end="")
    keys = bank_choice.keys()
    for i in keys:
        print(welcome_item.format(i,bank_choice[i]))
    print("**********************************")

# 输入帮助方法：chose是打印选项
def inputHelp(chose,datatype="str"):
    while True:
        print("请输入",chose,":")
        i = input(">>>:")
        if len(i) == 0:
            print("该项不能为空！请重新输入！")
            continue
        if datatype != "str":
            return int(i)
        else:
            return i

# 判断是否存在该银行选项
def  isExists(chose,data):
    if chose in data:
        return True
    return False


# 获取随机码
def  getRandom():
    li = "0123456789qwertyuiopasdfghjklzxcvbnmZXCVBNMASDFGHJKLQWERTYUIOP"
    string = ""
    for i in range(8):
        string =  string + li[int(random.random()* len(li))]
    return string

# 通过账号获取账户信息
def findByAccount(account):
    for i in bank.keys():
        if bank[i]["account"] == account:
            return i
    return None

# 银行的开户方法
def bank_addUser(username,password,country,province,street,door,money):
    # 查询是否已满
    sql = "select count(*) from pick"
    param = []
    data = select(sql,param)
    if data[0][0] >= 100:
        return 3
    # 查询是否存在
    sql1 = "select * from pick where username = %s"
    param1 = [username]
    data1 = select(sql1,param1)
    if len(data1) > 0:
        return 2
    # 插入数据
    sql2 = " insert into pick values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    param2 = [getRandom(),username,password,country,province,street,door,money,'2021-12-07',bank_name]
    update(sql2,param2)
    return 1

# 银行的存钱方法先根据传入的账号信息查询用户库里是否有该用户。若没有则返回False
# 若有，则将该用户的金额存进去。
def bank_saveMoney(account,money):
    sql3 = "select * from pick where account = %s"
    param3 = [account]
    data3 = select(sql3,param3)
    if len(data3) > 0:
        sql4 = "update pick set money = money + %s where account = %s"
        param4 = [money,account]
        update(sql4,param4)
        return True
    else:
        return False

# 银行的取钱功能先根据账号信息来查询该用户是否存在，若不存在，则返回代号1，
# 若存在，则继续判断密码是否正确，若不正确，则返回代号2。
# 若账号密码都正确，则继续判断当前用户的金额是否满足要取出的钱，若不满足，则返回代号3，
# 若满足，则将该用户的金额减去。
def bank_takeMoney(account,password,money):
    #查询该用户是否存在
    sql5 = "select * from pick where account = %s"
    param5 = [account]
    data5 = select(sql5, param5)
    #若存在，则继续判断密码是否正确
    if len(data5) > 0:
        sql6="select * from pick where pword = %s and account = %s"
        param6 = [password,account]
        data6 = select(sql6,param6)
        #若账号密码都正确，则继续判断当前用户的金额是否满足要取出的钱
        if len(data6) > 0:
            sql8 = "select * from pick where money > %s and account = %s"
            param8 = [money,account]
            data8 = select(sql8,param8)
            #若满足，则将该用户的金额减去
            if len(data8)>0:
                sql7 = "update pick set money = money - %s where account= %s "
                param7 = [money,account]
                update(sql7,param7)
            #若不满足，则返回代号3
            else:
                return 3
        #若账号密码不正确，则返回代号2
        else:
            return 2
    #若不存在，则返回代号1
    else:
        return 1


# 银行的查询功能先根据账号判断用户库是否存在该用户，若不存在则打印提示信息：该用户不存在。
# 否则继续判断密码是否正确。若不正确则打印相对应的错误信息。
# 若账号和密码都正确，则将该用户的信息都打印出来，比如：当前账号：xxxx,密码:xxxxxx,余额：xxxx元，用户居住地址：xxxxxxxxxxxxx，当前账户的开户行：xxxxxxxxxx.
def bank_selectUser(account,password):
    sql8 = "select * from pick where account = %s"
    param8 = [account]
    data8 = select(sql8, param8)
    # 若存在，则继续判断密码是否正确
    if len(data8) > 0:
        sql9 = "select * from pick where pword = %s and account = %s"
        param9 = [password, account]
        data9 = select(sql9, param9)
        # 若账号密码都正确，则将该用户的信息都打印出来
        if len(data9) > 0:
            for i in data9:
                print(i)
        else:
            print("用户密码错误！")
    else:
        print("该用户不存在！")

# 银行的转账功能先查询用户库是否存在转出和转入的账号，若不存在则返回代号,1，
# 若账号都存在则继续判断转出账号的密码是否正确，若不正确，则返回2，
# 若正确则继续判断要转出的金额是否足够，若不够则返回3，
# 否则正常转出，转出的账号用户金额要相对应的减少，转入的金额相对应的增加。
def bank_transformMoney(outputaccount,inputaccount,outputpassword,outputmoney):
    # 查询该用户是否存在
    sql10 = "select * from pick where account = %s"
    param10 = [outputaccount]
    data10 = select(sql10, param10)
    param15 = [inputaccount]
    data15 = select(sql10, param15)
    # 若outputaccount存在，则继续判断密码是否正确
    if len(data10) > 0 :
        sql11 = "select * from pick where pword = %s and account = %s"
        param11 = [outputpassword, outputaccount]
        data11 = select(sql11, param11)
        # 若账号密码都正确，则继续判断当前用户的金额是否满足要取出的钱
        if len(data11) > 0:
            sql12 = "select * from pick where money > %s and account = %s"
            param12 = [outputmoney, outputaccount]
            data12 = select(sql12, param12)
            # 若满足，则将该用户的金额减去
            if len(data12) > 0 and len(data15)>0:
                sql13 = "update pick set money = money - %s where account= %s "
                sql14 = "update pick set money = money + %s where account= %s "
                param13 = [outputmoney, outputaccount]
                update(sql13, param13)
                param14 = [outputmoney, inputaccount]
                update(sql14, param14)
            # 若不够则返回3
            else:
                return 3
        # 若账号密码不正确，则返回代号2
        else:
            return 2
    # 若不存在，则返回代号1
    else:
        return 1


# 开户方法
def  addUser():
    username = inputHelp("用户名")
    password = inputHelp("密码")
    country = inputHelp("居住地址：1.国家：")
    province =  inputHelp("省份")
    street = inputHelp("街道")
    door = inputHelp("门牌号")
    money =  inputHelp("银行卡余额","int")

    # 调用银行的开户方法完成开户操作  返回 1 2 3
    status = bank_addUser(username,password,country,province,street,door,money)
    # 判断1   2   3
    if status == 1:
        user = bank[username]
        print("恭喜开户成功！以下是您的开户信息：")
        print(myinfo.format(account=user["account"],
                            username=username,
                            password=user["password"],
                            country=user["country"],
                            province=user["province"],
                            street=user["street"],
                            door=user["door"],
                            money=user["money"],
                            bank_name=user["bank_name"]
                            ))
    elif status == 2:
        print("改用户已经存在！请携带证件到其他银行办理！谢谢！！！！！")
    elif status == 3:
        print("银行库已满！请携带证件到其他银行办理！谢谢！！！！！")

# 存钱
def saveMoney():
    account = inputHelp("账号")
    m =  inputHelp("存入的金额","int")

    flag = bank_saveMoney(account,m)

    if flag:
        print("存储成功!您的个人信息为：")
        uname = findByAccount(account)
        user = bank[uname]
        print(myinfo.format(account=user["account"],
                            username=uname,
                            password=user["password"],
                            country=user["country"],
                            province=user["province"],
                            street=user["street"],
                            door=user["door"],
                            money=user["money"],
                            bank_name=user["bank_name"]
                            ))
    else:
        print("对不起，您的个人信息不存在！请先开户后再次操作！")

# 取钱
def takeMoney():
    account = inputHelp("账户")
    password =  inputHelp("密码")
    tmoney = inputHelp("取出金额","int")

    f = bank_takeMoney(account,password,tmoney)

    if f == 1:
        print("改用户不存在！")
    elif f == 2:
        print("密码错误！")
    elif f == 3:
        print("取款金额不足！")
    elif f == 0:
        print("取款成功！")
        bank_selectUser(account,password)


# 转账功能
def transformMoney():
    output = inputHelp("转出的账号")
    input = inputHelp("转入的账号")
    outputpass =  inputHelp("转出的密码")
    outputmoney = inputHelp("要转出的金额","int")

    f = bank_transformMoney(output,input,outputpass,outputmoney)

    if f == 1:
        print("转出或转入的账号不存在！")
    elif f == 2:
        print("输入密码错误！")
    elif f == 3:
        print("转账金额不足！")
    else:
        print("转账成功！")
        print("您的个人信息：")
        bank_selectUser(output,outputpass)

# 查询账户方法
def selectUser():
    account = inputHelp("账号")
    password = inputHelp("密码")

    bank_selectUser(account,password)

# 核心程序
while True:

    print_welcome()
    chose = inputHelp("选项")
    if isExists(chose,bank_choice):
        if chose  == "1":
            addUser()
        elif chose == "2":
            saveMoney()
        elif chose == "3":
            takeMoney()
        elif chose == "4":
            transformMoney()
        elif chose == "5":
            selectUser()
        elif chose == "6":
            print("Bye,Bye您嘞！！！！")
            break
    else:
        print("不存在改选项，别瞎弄！")

