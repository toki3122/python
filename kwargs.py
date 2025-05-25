#kwargs are the same as args but they pack all the arguments into a dictionary
def hello(first,last):
    print("hello "+first+last)
hello(first="toki",last="3122")
#if we add a middle name to this, it will show error
def hello1(**kwargs):
    print("hello",end=" ")
    for key,value in kwargs.items():
        print(value,end=" ")
hello1(first="toki",middle="middle",last="3122")