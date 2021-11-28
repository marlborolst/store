for i in range(3):
    name=input("please input username:")
    password=input("please input password:")
    if name=="root" and password=="admin":
        print("ok!")
        break
    else:
        print("error!")
else:
    print("lock!")