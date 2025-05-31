#when a child class is derived from more than one parent class
class prey:
    def flee(self):
        print("this animal flees")
class predator:
    def hunt(self):
        print("this animal hunts")
class Rabbit(prey):
    pass
class Hawk(predator):
    pass
class Fish(prey,predator):
    pass
rabbit=Rabbit()
hawk=Hawk()
fish=Fish()
rabbit.flee()
hawk.hunt()
fish.hunt()
fish.flee()