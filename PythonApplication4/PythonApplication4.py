n=int(input())
x=1
condition=True
if n>1000 or n==0:
    print("wrong")
elif n==1:
    print("1=1")
elif n:
    print("{}=".format(n),end='')
    while n!=1:
        x+=1
        while n % x == 0:
            n/=x
            if condition:
                condition=False
                print(x,end='')
            else :
                print("*{}".format(x),end='')
