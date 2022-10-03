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
