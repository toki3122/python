#misc.
n=int(input("enter n: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        if i==1 or i==n or j==1 or j==i:
            print("*",end="")
        else:
            print(" ")
    print()
#cross:
n=int(input("enter n: "))
for i in range(n,0,-1):
    for j in range(1,n+1):
        if i==j or i+j==n+1:
            print("*",end="")
        else:
            print(" ",end="")
    print()
    #misc.
n=int(input("enter n: "))
for i in range(1,n+1):
    for j in range(1,n-i+1):
       print(" ",end="")
    for j in range(1,i+1):
        print(j,end="")
    for k in range(i-1,0,-1):
        print(k,end="")
    print()
for i in range(n-1,0,-1):
    for j in range(1,n-i+1):
       print(" ",end="")
    for j in range(1,i+1):
        print(j,end="")
    for k in range(i-1,0,-1):
        print(k,end="")
    print()
    #heart:
n=int(input("enter n: "))
for i in range(round(n/2),n,2):
    for j in range(1,n-1,3):
        print(" ",end="")
    for k in range(1,i+1):
        print("*",end="")
    for k in range(i,n-i+1,2):
        print(" ",end="")
    for k in range(1,i+1):
        print("*",end="")
    print()
for i in range(n,0,-1):
    for j in range(1,n-i+1):
        print(" ",end="")
    for j in range(1,2*i):
        print("*",end="")
    print()