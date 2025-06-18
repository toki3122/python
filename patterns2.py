#misc.
n=int(input("enter n: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(" "+str(i*j),end="")
    print()
#pyramidy
n=int(input("enter n: "))
for i in range(1,n+1):
    for j in range(1,n-i+1):
       print("  ",end="")
    for j in range(1,2*i):
        print(" "+str(i),end="")
    print()
#diamond:
n=int(input("enter n: "))
for i in range(1,n+1):
    for j in range(1,n-i+1):
       print("  ",end="")
    for j in range(1,2*i):
        print(" "+str(i),end="")
    print()
for i in range(n-1,0,-1):
    for j in range(1,n-i+1):
       print("  ",end="")
    for j in range(1,2*i):
        print(" "+str(i),end="")
    print()
#triangle:
n=int(input("enter n: "))
for i in range(1,n+1):
    for j in range(1,n-i+1):
       print(" ",end="")
    for j in range(1,i+1):
        print(str(i)+" ",end="")
    print()
#diamond:
n=int(input("enter n: "))
for i in range(1,n+1):
    for j in range(1,n-i+1):
       print(" ",end="")
    for j in range(1,i+1):
        print(str(i)+" ",end="")
    print()
for i in range(n-1,0,-1):
    for j in range(1,n-i+1):
       print(" ",end="")
    for j in range(1,i+1):
        print(str(i)+" ",end="")
    print()
n=int(input("enter n: "))
for i in range(1,n+1):
    for j in range(1,n-i+1):
       print(" ",end="")
    for j in range(1,i+1):
        print(str(i)+" ",end="")
    print()
#empty square
n=int(input("enter n: "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or j==1 or j==n:
            print("*",end="")
        else:
            print(" ",end="")
    print()