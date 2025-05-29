import os
source='F:\\tokee\\programming\\python\\code\\copy.txt'
destination='F:\\tokee\\programming\\copy.txt'
try:
    if os.path.exists(destination):
        print("there is already a file there")
    else:
        os.replace(source,destination)
        print(source+" was moved")
except FileNotFoundError:
    print(source+" was not found")