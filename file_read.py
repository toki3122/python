try:
    with open('F:\\tokee\\programming\\python\\code\\2.txt') as file:
        print(file.read())
except FileNotFoundError:
    print("file not found")
