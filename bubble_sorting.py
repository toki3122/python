n=int(input("enter the number of inputs: "))
array=[]
for i in range(n):
    arr=input("entry no. "+str(i+1)+": ")
    array.append(arr)
for i in range(n-1):
    for j in range(n-1):
        if array[j]<array[j+1]:
            temp=array[j]
            array[j]=array[j+1]
            array[j+1]=temp
print("data after descending sort:\n")
for i in array:
    print(i)
for i in range(n-1):
    for j in range(n-1):
        if array[j]>array[j+1]:
            temp=array[j]
            array[j]=array[j+1]
            array[j+1]=temp
print("data after ascending sort:\n")
for i in array:
    print(i)
