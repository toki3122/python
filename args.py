#args is a parameter that will pack all arguments into a tuple
#useful so that a function can accept a varying amount of arguments

def add(num1,num2):
    return num1+num2
print(add(1,2))
#users HAVE to enter two variables, otherwise there will be type error
#we can use arg so that a user can enter variable number of inputs
def add1(*arg): #HAVE TO HAVE "*"
    sum=0
    for i in arg:
        sum+=i
    return sum
print(add1(1,2,3,4,5,6))
#as the values turn into tuples, the set of values cannot be changed
#to change it, we have to cast the tuple
def add2(*arg):
    sum=0
    arg=list(arg)
    arg[0]=0
    for i in arg:
        sum+=i
    return sum
print(add2(1,2,3,4,5,6))