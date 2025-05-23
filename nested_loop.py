rows=int(input("row: "))
columns=int(input("column: "))
symbol=input("symbol: ")
for i in range(rows):
    for j in range(columns):
        print(symbol,end="")#end lets things print in a line
    print()#this lets to go to the next line