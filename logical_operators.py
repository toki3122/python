#to check multiple logic statements
temp=int(input("what is the temp outside?: "))
if not(temp>=0 and temp<=30):
    print("bad temp")
elif not(temp>30 or temp<0):
    print("good temp")
#not just reverses the conditions