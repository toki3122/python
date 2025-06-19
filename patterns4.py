import math
#floyd's triangle:
n=int(input("enter n: "))
m=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(m,end=" ")
        m+=1
    print()
#pascal's triangle-1:
n=int(input("enter n: "))
for i in range(n):
    for j in range(1,n-i+1):
        print(" ",end="")
    print(pow(11,i),end="")
    print()
#pascal's triangle-2:
n=int(input("enter n: "))
for i in range(1,n+1):
    m=1
    for j in range(1,n-i+1):
        print(" ",end="")
    for j in range(1,i+1):
        print(m,end=" ")
        m=int(m*(i-j)/j)
    print()
#heart:
n=int(input("enter n: "))
for i in range(math.floor(n/2),n+1,2):
    for j in range(n-i-1,0,-1):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end="")
    for j in range(n-i,0,-1):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end="")
    print()
for i in range(n,0,-1):
    for j in range(1,n-i+1):
        print(" ",end="")
    for j in range(1,2*i):
        print("*",end="")
    print()