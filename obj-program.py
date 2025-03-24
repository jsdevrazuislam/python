class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student('razu', 20)
print(student1.name, student1.age)

class Book:
    def __init__(self, name, writer_name):
        self.name = name
        self.writer_name = writer_name

    def show_info(self):
        print(f"Book name is {self.name} and Writer Name is {self.writer_name}")

book = Book("New", "Razu")
book.show_info()

class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def area_finder(self):
        print(f"Your Area {self.x * self.y}")

class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    def deposit(self, num):
        self.balance += num
    def withdraw(self, num):
        if num > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= num
            print(f"balance withdraw {num}")

account = BankAccount(100)
account.deposit(200)
account.withdraw(500)

# task 1
class Person:
    def __init__(self):
        self.__age = 0
    def set_age(self, age):
        if age == 0 or age < 0:
            print("Invalid age")
        else:
            self.__age = age
    def get_age(self):
        return self.__age
    
person = Person()
person.set_age(100)
print(person.get_age())

# task 2
class Car:
    def __init__(self):
        self.__speed = 0
    def increase_speed(self, amount):
        if amount == 0 or amount > 200:
            print("Invalid Speed")
        else:
            self.__speed = amount
    def get_speed(self):
        return self.__speed
    
car = Car()
car.increase_speed(200)
print(car.get_speed())

# task 3
class User:
    def __init__(self):
        self.__password = ''
    def set_password(self, password):
        self.__password = password
    def check_password(self, password):
        if self.__password == password:
            return "Password Correct"
        else:
            return "Invalid Password"
user1 = User()
user1.set_password('password')
print(user1.check_password('password'))

# task 1

class Vehicle:
    def start_engine(self):
        print('yoo')

class Car(Vehicle):
    def honk(self):
        print("Hook")

car = Car()
car.honk()


# task 2
class Teacher:
    def my_teacher(self):
        print('My Teacher')
class Researcher:
    def my_research(self):
        print("my research")

class Professor(Teacher, Researcher):
    def my_professor(self):
        print('Professor')

test = Professor()
test.my_research()
test.my_professor()
test.my_teacher()

# task 3
class LivingBeing:
    def livingBeing(self):
        print("LivingBeing")

class Animal(LivingBeing):
    def animal(self):
        print("Animal")

class Dog(Animal):
    def dog(self):
        print("Dog")
# task 4
class Person:
    def person(self):
        pass

class Student(Person):
    def student(self):
        pass

class Teacher(Person):
    def teacher(self):
        pass

# Bonus Task
class Bird:
    def fly():
        print("Birds can fly")

class Penguin(Bird):
    def fly():
        print("Penguins cannot fly")

# task 1

class Vehicle:
    def __init__(self,brand, model):
        self.brand = brand
        self.model = model

class Car(Vehicle):
    def __init__(self, brand, model, year):
        super().__init__(brand, model)
        self.year = year


class Animal:
    def __init__(self):
        pass
    def speak(self):
        pass

class Dog(Animal):
    def __init__(self):
        super().__init__()

    def speak(self):
        print("Woof!")

class Cat(Animal):
    def __init__(self):
        super().__init__()

    def speak(self):
        print("Meow!")

class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    def balance(self):
        print("balance")

class SavingsAccount(BankAccount):
    def __init__(self, balance):
        super().__init__(balance)

    def balance(self):
        print(self.balance + self.balance / 5)

# task 1
class Shape:
    def area(self):
        print('area')

class Circle(Shape):
    def area(self):
        print('circle area')

class Rectangle(Shape):
    def area(self):
        print("Rectangle area")

obj1 = Shape().area()
obj2 = Circle().area()
obj3 = Rectangle().area()


# task 2
class Calculator:
    def multiply(self, *args):
        result = 1
        for x in args:
            result *= x
        print(result)


obj4 = Calculator().multiply(5,10,20)

# task 3
class Employee:
    def get_salary(self):
        print("Get Employee Salary")

class FullTimeEmployee(Employee):
    def get_salary(self):
        print("Get FullTimeEmployee")

class PartTimeEmployee(Employee):
    def get_salary(self):
        print("Get PartTimeEmployee")


obj5 = Employee().get_salary()
obj6 = FullTimeEmployee().get_salary()
obj7 = PartTimeEmployee().get_salary()

# task 1

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        return 'Hello'
    
class Dog(Animal):
    def sound(self):
        return "Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow!"
    
dog = Dog()
cat = Cat()

print(dog.sound())
print(cat.sound())
