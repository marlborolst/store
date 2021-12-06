#编写一个函数
l=[21,56,56,10,56,21,56,21,56,10,56,10,56,56,56]
dict_l = {}
def add(l):
    #传入一个列表
    for i in l:
        if i not in dict_l:
            dict_l[i]=1
        else:
            #统计每个数字出现的次数
            dict_l[i]+=1
    #返回字典数据
    return dict_l
print(add(l))