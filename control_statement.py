#break= to terminate the loop
#continue=skips the next iteration for the loop
#pass=does nothing but acts as a placeholder
while True:
    name=input("enter your name: ")
    if name!="":
        break
phone_number="123-456-7890"
for i in phone_number:
    if i=="-":
        continue
    print(i,end="")
for i in range(1,21):
    if i==13:
        pass
    else:
        print(i)