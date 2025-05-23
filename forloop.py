import time
#while loop= unlimited
#for loop=limited
#for *iterator* in range(start,end,step):
#no start, no step:
for i in range(10):#value of i to 10-1 times
    print(i+1)
#no step:
for i in range(50,100):
    print(i)
for i in range(50,100,2):
    print(i)
#a benefit of for loop is it can iterate anything(string, letters in a string, or any sort of collection)
for i in "toki3122":
    print(i)
for i in range(10,0,-1):
    print(i)
    time.sleep(1)#delay for 1s
print("happy new year!!")