#请编程统计列表中的每个数字出现的次数(百度初级测试开发笔试题)
list = [1,4,7,5,8,2,1,3,4,5,9,7,6,1,10]
l={}
def add(list):
    for i in list:
        if i in l:
            l[i]=l[i]+1
        else:
            l[i]=1
    return l
print(add(list))