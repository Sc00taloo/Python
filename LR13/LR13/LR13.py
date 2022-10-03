#7
class Animal():
    name=""
    def __init__(self):
        print("Родилось животное")

class Cat(Animal):
    def makeNoise(self):
        print(self.name, "говорит мяу")
    def eat(self):
        print("Намнём")

class Dog(Animal):
    def makeNoise(self):
        print(self.name, "говорит гав")
    def eat(self):
        print("Намнём")

class simpleAnimal(Animal):
    def makeNoise(self):
        print(self.name, "говорит гррр")
    def eat(self):
        print("Намнём")

myCat = Cat()
myDog = Dog()
myDog2 = Dog()
myAnimal = simpleAnimal()
myCat.name = "Chmonya"
myDog.name = "Kirieshka"
myDog2.name = "Bimbos"
myAnimal.name = "Pudg"

myCat.makeNoise()
myCat.eat()
myDog.makeNoise()
myDog.eat()
myDog2.makeNoise()
myDog2.eat()
myAnimal.makeNoise()
myAnimal.eat()

#6
class Animal():
    name=""
    def __init__(self):
        print("Родилась собака")

class Dog(Animal):
    def makeNoise(self):
        Animal.__init__(self)
        print(self.name, "говорит гав")

myDog = Dog()
myDog.name = "Kirieshka"
myDog.makeNoise()

#5
class Animal():
    name=""
    def __init__(self):
        print("Родился кот")

class Cat(Animal):
    def makeNoise(self):
        Animal.__init__(self)
        print(self.name, "говорит мяу")

myCat = Cat()
myCat.name = "Chmonya"
myCat.makeNoise()

#4
class Point:  
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    def dist(self, point):
        return ((self.x - point.x)**2 + (self.y - point.y)**2)**0.5

pos1 = Point(3, 1)
pos2 = Point(2, 1)
print(pos1.dist(pos2))
print("sTOP")

#3
class StringVar():
    def __init__(self, input_name):
        self.hidden_name = input_name
    #def get_name(self):
    #    print('внутри getter')
    #    return self.hidden_name
    @property
    def name(self):
        print('внутри getter')
        return self.hidden_name
    #def set_name(self, input_name):
    #    print('внутри setter')
    #    self.hidden_name = input_name
    @name.setter
    def name(self, input_name):
        print('внутри setter')
        self.hidden_name = input_name
    #name = property(get_name, set_name)

test = StringVar("Eating")
print(test.name)
#print(test.get_name())
test.name = "Siting"
print(test.name)
#test.set_name("Bruh")
#print(test.name)

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