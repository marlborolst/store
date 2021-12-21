import time
f1 = open(file="baidu_x_system.txt",mode="r+",encoding="utf-8")
f2 = open(file="IPtime.txt",mode="w+",encoding="utf-8")
txt = []#空列表
iptime={}#空字典
for l in f1.readlines():
    l=l.split()
    txt.append(l)#添加到列表
while True:
    for i in range(len(txt)):
        iptime[txt[i][0]] = 1     #第一个ip访问1次（往空字典里添加键值）
        #      IP（键）    次数（值）
    for i in iptime:
        # print(i){ip}
        # print(iptime[i]){次数}
        for y in range(len(txt)):
            if i==txt[y][0]:
                iptime[i]+=1
        print("用户ip为：",i,"访问了",iptime[i],"次")
        f2.write("用户ip为；")
        f2.write(i)
        f2.write("访问次数为；")
        f2.write(str(iptime[i]))
        f2.write("\n")
    time.sleep(30)




