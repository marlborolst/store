a=int(input('输入行数'))
l=[]
for i in range(a):#循环a赋值给i
    h=[1]
    l.append(h)#把h添加到l
    if i==0:
        print(h)
        continue
    for y in range(1,i):
        h.append(l[i-1][y-1]+l[i-1][y])
    h.append(1)#把1添加到[h]的最后一位
    print(h)