#lists= to save multiple items in a single variable
#works just as arrays
food=["pizza","burger","hotdog","spaghetti"]
print(food)
print(food[2])
food[0]="sushi" #overrides the value in 0th index
print(food[0])
food.append("ice cream")#adds another item
print("append:")
print("")
for x in food:
    print(x)
food.remove("hotdog")
print("")
print("remove:")
print("")
for x in food:
    print(x)
food.pop()#deletes the last element
print("")
print("pop:")
print("")
for x in food:
    print(x)
food.insert(0,"cake")#inserts new data in list
print("")
print("insert:")
print("")
for x in food:
    print(x)
print("")
print("sort:")
print("")
food.sort()
for x in food:
    print(x)
print("")
print("clear:")
print("")
food.clear()
for x in food:
    print(x)