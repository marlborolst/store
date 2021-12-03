import random
l=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
i=0
s=6
while True:
    a = random.randrange(len(l))
    num=random.randint(0,9)
    if s>3:
        s=s-1
        print(l[a])
        i=i+1
    elif i<6:
        i=i+1
        print(num)
