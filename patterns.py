#equilateral
n=int(input("enter n: "))
for i in range(0,n):
    for j in range(i+1):
        print("*",end="")
    print()
#row no.
n=int(input("enter n: "))
for i in range(1,n+1):
    for j in range(i):
        print(" "+str(i),end="")
    print()
#col no.
for i in range(1,n+1):
    for j in range(1,i+1):
        print(" "+str(j),end="")
    print()
n=int(input("enter n: "))
#0,1 row
for i in range(1,n+1):
    for j in range(i):
        print(" "+str(i%2),end="")
    print()
#0,1 col
for i in range(1,n+1):
    for j in range(i):
        print(" "+str(j%2),end="")
    print()
n=int(input("enter n: "))
#alphabetical_row
for i in range(1,n+1):
    for j in range(1,i+1):
        print(" "+chr(64+i),end="")
    print()
#alphabetical_col
for i in range(1,n+1):
    for j in range(1,i+1):
        print(" "+chr(64+j),end="")
    print()
n=int(input("enter n: "))
#col no. reverse
n=int(input("enter n: "))
for i in range(n+1,1,-1):
    for j in range(1,n-i+1):
       print(" ",end="")
    for j in range(1,i):
        print(" "+str(j),end="")
    print()
#row no. reverse
n=int(input("enter n: "))
for i in range(n+1,1,-1):
    for j in range(1,n-i+1):
       print(" ",end="")
    for j in range(1,i):
        print(" "+str(i-1),end="")
    print()
#reverse
for i in range(n,0,-1):
    for j in range(1,n-i):
       print(" ",end="")
    for j in range(0,i):
        print("*",end="")
    print()
#big triangle:
n=int(input("enter n: "))
for i in range(0,n):
    for j in range(i+1):
        print("*",end="")
    print()
for i in range(n,0,-1):
    for j in range(1,i):
        print("*",end="")
    print()
