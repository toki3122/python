#function calls inside other function calls, innermost function calls are resolved first
#returned value is used as argument for the next outer function
num=input("enter a whole positive number: ")
num=float(num)
num=abs(num)
num=round(num)
print(num)
#this can be done in one line
print(round(abs(float(input("enter a whole positive number: ")))))