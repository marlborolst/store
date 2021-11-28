while True:
 a=int(input("输入a："))
 b=int(input("输入b："))
 c=int(input("输入c："))

 if (a+b>c)and(a+c>b)and(b+c>a):
    if a==b==c:
       print("等边三角形")
    elif(a==b or a==c or c==b):
       print("等腰三角形")
    elif(a*a+b*b==c*c)or(a*a+b*b==c*c)or(b*b+c*c==a*a):
        print("直角三角形")
    else:
        print("普通三角形")
 else:
    print("不构成三角形")


