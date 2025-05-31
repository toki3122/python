class animal:
    alive=True
    def eat(self):
        print("this animal is eating")
    def sleep(self):
        print("this animal is sleeping")
class Rabbit(animal):
    def run(self):
        print("this animal is running")
class Fish(animal):
    def swim(self):
        print("this animal is swimming")
class Hawk(animal):
    def fly(self):
        print("this animal is flying")
rabbit=Rabbit()
fish=Fish()
hawk=Hawk()
print(rabbit.alive)
fish.eat()
hawk.sleep()
rabbit.run()
fish.swim()
hawk.fly()