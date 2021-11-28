sum=0
max=0
a=0
for i in range(1,11):
    i=int(input("输入："))
    sum=sum+i
    a=sum/i
    if i>max:
        max=i
        print("求和：",sum)
        print("平均值",a)
        print("最大值",max)