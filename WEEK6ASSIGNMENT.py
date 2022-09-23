# QUESTION 1

class Credit_Card:
    def __init__(self, card_number, expiration_date, security_code):
        self.card_number = card_number
        self.expiration_date = expiration_date
        self.security_code = security_code
        
    def info(self):
        return f"Number: {self.card_number}\nExp Date: {self.expiration_date}\nSec Code: {self.security_code}"

card = Credit_Card("72343456", "27/08/2025", "19658")

card.info()

# question 2

class Animal:
     def __init__(self, name):
         self.name = name

class Dog(Animal):
     def __init__(self, name):
         super().__init__(name)

     def bark(self):
         return f"{self.name} is barking"

dog = Dog("Snoop")
dog.bark()
print(dog.bark())

# question 5

class Employee:
     def __init__(self, name, age, address):
         self.name = name
         self.age  = age
         self.address = address
        
     def eat(self):
         print(f"{self.name} is eating")

     def sleep(self):
         print(f"{self.name} is sleeping")

     def work(self):
         print(f"{self.name} is working")

    
e = Employee("Jumanji", 31, 700000)
e.eat()
e.sleep()
e.work()

# question 7

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year  = year
    

    def start(self):
        print(f"{self.make},{self.model}, {self.year} is starting")

    def stop(self):
        print(f"{self.make},{self.model}, {self.year} is stopping")

    def drive(self):
        print(f"{self.make},{self.model}, {self.year} is driving")

    
class Car(Vehicle):
    def __init__(self, make, model, year, color):
        self.color = color
        super().__init__(make, model, year)

    def start(self):
        return super().start()
        
    def stop(self):
        return super().stop()
        
    def drive(self):
        return super().drive()
    

    # make, model, year, and color of the car and the word "is parking".
    def park(self):
        print(f"{self.make}, {self.model}, {self.year}, {self.color} is parking")


car = Car("KIA", "A-class", 2022, "brown")
car.start()
car.stop()
car.drive()
car.park()

# question 8

class Animal:
    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age  = age
    
    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")
    
    def make_sound(self):
        print(f"{self.name} is making a sound")

class Dog(Animal):
    def __init__(self, name, color, age, breed):
        self.breed = breed
        super().__init__(name, color, age)

    def eat(self):
        return super().eat()

    def sleep(self):
        return super().sleep()
        
    def make_sound(self):
        return super().make_sound()

    def bark(self): 
        print(f"{self.name} is barking")
    

dog = Dog("snoop", "Brown", 3, "German")

dog.eat()
dog.sleep()
dog.make_sound()
dog.bark()
