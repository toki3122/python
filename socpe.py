#the region that a variable is recognized is the scope
#a variable is only available from inside the region it is created
name="toki" #global scope(available from inside or outside of a function)
def display_name():
    name="3122" #local scope(only available inside the function)
    print(name)
print(name)
display_name() #if there was no "name" variable inside the function, then it would have printed the global variable
#functions follow LEGB rule for variables
#L=Local
#E=Enclosing
#G=Global
#B=Built-in
