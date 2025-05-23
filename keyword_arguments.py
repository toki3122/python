#arguments preceded by an identifier when we pass them to a function
#the order of the arguments does not matter,unlike positional arguments
#python knows the names of the arguments that our function receives
def hello(first,middle,last):
    print("hello "+first+" "+middle+" "+last)
hello("bro","dude","code")
hello("code","bro","dude")
#as we can see, the change in input position changes the output
hello(last="code",middle="dude",first="bro")
#position will not matter anymore