import os
path="F:\\tokee\\programming\\python\\code\\assets\\name.txt"
if os.path.exists(path):
    print("that location exists!!")#location detection
    if os.path.isfile(path):
        print("that is a file")#file detection
    elif os.path.isdir(path):
        print("this is a directory!")#folder detection
else:
    print("that location does not exists!!")