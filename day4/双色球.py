import random
red=[]
z=int(input('选几注'))
for i in range(z):
    while True:
        a=random.randint(1,33)
        if a not in red:
            red.append(a)
            if len(red)==6:

                for x in range(len(red)-1):
                    for y in range(x+1,len(red)):
                        if red[x]>red[y]:
                            red[x],red[y]=red[y],red[x]


                b=random.randint(1,15)
                red.append(b)
                print(red)

        if len(red)==7:
            red=[]
            break

