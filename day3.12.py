#用循环来实现20以内的数的阶乘。（1! +2!+3!+…..+20!）
while True:
  a=int(input("input:"))
  b=a
  sum=0
  while True:
      a=a-1
      if a>0:
        while True:
            if b>0:
                c=b*(b-1)
                sum=sum+c
                b=b-1
                continue
            else:
                break
        b=a
      else:
        print(sum)
        break