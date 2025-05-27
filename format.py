#optional method that gives users more control when displaying output
animal="cow"
item="moon"
print("the "+animal+" jumped over the "+item)
print("the {} jumped over the {}".format(animal,item))#positional argument
print("the {1} jumped over the {0}".format(animal,item))
#we can also use keywords
print("we can go {one} and then {two}".format(one="lala",two="lalala"))
text="the {} jumped over the {}"
print(text.format(animal,item))
#padding
name="toki"
print("hello,my name is {:10},nice to meet you".format(name))
print("hello,my name is {:<10},nice to meet you".format(name))#left align
print("hello,my name is {:>10},nice to meet you".format(name))#right align
print("hello,my name is {:^10},nice to meet you".format(name))#center align
print("hello,my name is {0:10},nice to meet you".format(name))
num1=3.14159
print("pi is {:.2f}".format(num1))
num=1000
print("the number is {:,}".format(num))#with comma
print("the number is {:b}".format(num))#binary display
print("the number is {:o}".format(num))#octal display
print("the number is {:x}".format(num))#lowercase hex display
print("the number is {:X}".format(num))#uppercase hex display
print("the number is {:e}".format(num))#scientific notation
