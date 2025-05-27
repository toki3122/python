#exception=events detected during execution that interrupt the flow of the program
#numerator=int(input("enter a number to divide: "))
#denominator=int(input("enter a number to divide by: "))
#result=numerator/denominator
#print(result)
#if we 5/0, then it will be called an exception
try:   
    numerator=int(input("enter a number to divide: "))
    denominator=int(input("enter a number to divide by: "))
    result=numerator/denominator
except ZeroDivisionError:
    print("you cannot divide by zero!!")
except ValueError:
    print("enter only numbers please!")
except Exception:
    print("something went wrong T-T")
    #it is considered good practice to handle specific exceptions first
else:
    print(result)   
finally:
    print("works or not this will always execute")