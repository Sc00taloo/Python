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
print("stop")
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