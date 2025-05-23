#gives access to a sequence's element(str,list,tuples)
name="toki3122"
if(name[0].islower()):
    name=name.capitalize()
print(name)
first_name=name[:4].upper()#slicing
last_name=name[4:]#slicing
print(first_name)
print(last_name)
#neg indexing is also possible
print(name[-1])