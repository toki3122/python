#set is a collection which is unordered, unindexed, and has no duplicate values
#so they just shuffle around every time we print them
#operates faster than the others
utensils={"fork","spoon","knife"}
dishes={"bowl","plate","cup"}
for i in utensils:
    print(i)
utensils1={"fork","spoon","knife","knife","knife"}
for i in utensils1:
    print(i)#will print knife only once
print("")
utensils.remove("fork")
for i in utensils:
    print(i)
print("")
utensils.add("fork")
for i in utensils:
    print(i)
print("")
#utensils.clear()
utensils.update(dishes)#updates value from dishes
for i in utensils:
    print(i)
#we can also do this
print("")
dinner_table=utensils.union(dishes)
for i in dinner_table:
    print(i)
dishes.add("knife")
print("")
print(utensils.difference(dishes))#things that utensils have but dishes does not
print("")
print(utensils.intersection(dishes))#things they have in common
