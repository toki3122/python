import time
import math
print("series program \ninitializing...")
for i in range(11):
    print("-",end="")
    time.sleep(1)
print()
print("1:- 1+2+3+4+5+...+n")
print("2:- 1^2+2^2+3^2+...+n^2")
print("3:- 1^3+2^3+...+n^3")
print("4:- 1-2+3-4+5+...+n")
print("5:- 1^2-2^2+3^2+...+n^2")
print("6:- 1^3-2^3+...+n^3")
print("7:- factorial")
print("8:- 1^1+2^2+3^3+...+n^n")
print("9:- fibonacci sequence")
print("10:- fibonacci addition")
m=int(input("your choice:"))
if m==1:
    n=int(input("enter n: "))
    sum=0
    for i in range(n+1):
        sum+=i
    print("answer: "+str(sum))
elif m==2:
    n=int(input("enter n: "))
    sum=0
    for i in range(n+1):
        sum+=i*i
    print("answer: "+str(sum))
elif m==3:
    n=int(input("enter n: "))
    sum=0
    for i in range(n+1):
        sum+=i*i*i
    print("answer: "+str(sum))
elif m==4:
    n=int(input("enter n: "))
    sum=0
    for i in range(n+1):
        if i%2==0:
            sum-=i
        else:
            sum+=i
    print("answer: "+str(sum))
elif m==5:
    n=int(input("enter n: "))
    sum=0
    for i in range(n+1):
        if i%2==0:
            sum-=i*i
        else:
            sum+=i*i
    print("answer: "+str(sum))
elif m==6:
    n=int(input("enter n: "))
    sum=0
    for i in range(n+1):
        if i%2==0:
            sum-=i*i*i
        else:
            sum+=i*i*i
    print("answer: "+str(sum))
elif m==7:
    n=int(input("enter n: "))
    sum=1
    for i in range(1,n+1):
        sum*=i
    print("answer: "+str(sum))
elif m==8:
    n=int(input("enter n: "))
    sum=0
    for i in range(0,n+1):
        sum+=pow(i,i)
    print("answer: "+str(sum-1))
elif m==9:
    n=int(input("enter n: "))
    num1=0
    num2=1
    print(num1,end=" ")
    print(num2,end=" ")
    for i in range(n-2):
        temp=num1+num2
        num1=num2
        num2=temp
        print(num2,end=" ")
elif m==10:
    n=int(input("enter n: "))
    num1=0
    num2=1
    sum=1
    for i in range(n-2):
        temp=num1+num2
        num1=num2
        num2=temp
        sum+=num2
    print("answer: "+str(sum))
