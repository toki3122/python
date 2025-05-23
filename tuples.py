#tuples are a collection which is ordered and unchangeable
#used to group together related data
student=("toki",21,"male")
print(student.count("toki"))
print(student.index("male"))
for x in student:
    print(x)
if "toki" in student:
    print("toki was here")