print("" + "\n-------------------------OUTPUT-------------------------")
print("")
class Dog():
    species = 'Mammal'
    def __init__(self, breed, dname, spots):
        self.breed = breed
        self.dname = dname
        self.spots = spots

    def bark(self, number):
        print(f'My Name is {self.dname} and my tag is {number}')

mydog = Dog('Labrador', 'Milo', False)

print(mydog.breed)
print(mydog.species)
mydog.bark(5)

class Circle():
    pi = 3.14
    def __init__(self, radius):
        self.radius = radius
        self.area = radius * radius * 2
    def circum(self):
        return self.radius * self.pi * 2
myCircle = Circle(1)
cirum = myCircle.circum()
print(f'Circumference is {cirum}')
area = myCircle.area
print(f"Area is {area}")

class Animal():
    def __init__(self):
        print("")
        print("Animal Created")
    def aniType(self, aType):
        print(f"Animal type is {aType}")
    def aniColor(self, aColor):
        print(f"Animal Color is {aColor}")

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)

myDog = Dog()
myDog.aniType('Dog')
myDog.aniColor('White')


print("" + "\n-----------------------END OUTPUT-----------------------")
print("")