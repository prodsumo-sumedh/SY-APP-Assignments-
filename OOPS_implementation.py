class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner       
        self.balance = balance   

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdraw {amount}. Remaining balance: {self.balance}")
        else:
            print("Insufficient balance!")

# Creating objects (instances)
acc1 = BankAccount("Alice", 5000)
acc2 = BankAccount("Bob", 2000)

acc1.deposit(1500)
acc2.withdraw(1000)   

#Output
'''Deposited 1500. New balance: 6500
Withdraw 1000. Remaining balance: 1000'''





class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Usage
animals = [Dog("Buddy"), Cat("Whiskers")]
for animal in animals:
    print(animal.speak())  

#Output
'''Buddy says Woof!
Whiskers says Meow!'''





class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start_engine(self):
        print(f"The {self.brand} engine is running.")

# Child Class inheriting from Vehicle
class Car(Vehicle):
    def honk(self):
        print("Beep beep!")


my_car = Car("Toyota")
my_car.start_engine()  
my_car.honk()     



#Output
'''
The Toyota engine is running.
Beep beep!
'''