class animal:
    def eat(self):
        print("this animal is eating")
class Rabbit(animal):
    def eat(self):
        print("this rabbit is eating a carrot")
rabbit=Rabbit()
rabbit.eat()