#extracting a substring from a string
#indexing[] or slice()
#[start:stop:step]
name="toki 3122"
first_name=name[0:4]#will stop at (stop-1)th character
print(first_name)
print(name[:4])#can also be written as this
last_name=name[5:9]
print(last_name)
print(name[5:])
#steps determine how many steps after we take a character
funky_name=name[0:9:2]
print(funky_name)
print(name[::2])
#negative step would reverse the order of the substring
print(name[::-1])
website1="http://github.com"
website2="http://wikihow.com"
slice=slice(7,-4)#here negative indexing was done, negative indexing start with -1
print(website1[slice])
print(website2[slice])