#dictionary is a changeable, unordered collection of unique keyvalue pairs
#they are fast due to the use of hashing, allow us to access a value quickly
capitals={'USA':'washington DC',
          'india':'new dehli',
          'China':'Beijing',
          'Russia':'Moscow'}
#to check the dictionary:
#print(capitals['Germany'])
#as there is no  germany in dictionary,
#that ruins the flow of the code, gives error
#so instead:
print(capitals.get('Germany'))
print(capitals.keys())#prints the key value
print(capitals.values())#prints the value of key values
#to print the whole dictionary:
print(capitals.items())
#or
for key,value in capitals.items():
    print(key,value)
print("")
capitals.update({'Germany':'Berlin'})
for key,value in capitals.items():
    print(key,value)
print("")
#we can even update existing values
capitals.update({'USA':'Las Vegas'})
for key,value in capitals.items():
    print(key,value)
capitals.pop('india')#removes value
print("")
for key,value in capitals.items():
    print(key,value)
capitals.clear()
for key,value in capitals.items():
    print(key,value)