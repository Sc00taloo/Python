#2
class Animal():
    name=""
    def __init__(self, newName):
        self.name = newName
        print("Роилось животное", newName)
    def setName(self, newName):
        self.name = newName
    def getName(self):
        return self.name
    def eat(self):
        print("Намнём")
    def makeNoise(self):
        print(self.name, "говорит Гррр")

myAnimal = Animal("Baget")
print(myAnimal.getName())

myAnimal.setName("Packet")
print(myAnimal.getName())

myAnimal.eat()
myAnimal.makeNoise()

#1
class Cat():
    name=""
    color=""
    weight=0
    def meow(self):
        print(self.name, "говорит мяу")

myCat = Cat()
myCat.name = "Chmonya"
myCat.color = "Black with white"
myCat.weight = 5

myCat.meow()