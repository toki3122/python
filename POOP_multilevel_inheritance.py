#child class inherits another child class
class organism:
    alive=True
class animal(organism):
    def eat(self):
        print("this animal is eating")
class Dog(animal):
    def bark(self):
        print("this dog is barking")
dog=Dog()
print(dog.alive)
dog.eat()
dog.bark()