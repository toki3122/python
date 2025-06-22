import math
#void diamond:
n=int(input("enter n: "))
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end="")
    for j in range(1,2*i):
        if j==1 or j==2*i-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()
for i in range(n-1,0,-1):
    for j in range(1,n-i+1):
        print(" ",end="")
    for j in range(1,2*i):
        if j==1 or j==2*i-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()
#void triangle:
n=int(input("enter n: "))
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end="")
    for j in range(1,2*i):
        if j==1 or j==2*i-1 or i==1 or i==n:
            print("*",end="")
        else:
            print(" ",end="")
    print()
#cross:
n=int(input("enter n: "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==math.ceil(n/2) or j==math.ceil(n/2):
            print("*",end="")
        else:
            print(" ",end="")
    print()
#number void tiangle:
n=int(input("enter n: "))
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end="")
    for j in range(1,2*i):
        if j==1 or i==1 or i==n:
            print(j,end="")
        elif j==2*i-1:
            print("2",end="")
        else:
            print(" ",end="")
    print()