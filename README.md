# Python Learning Journey

এই ডকুমেন্টে Python-এ যা যা শিখেছি তার সংক্ষিপ্ত বিবরণ ও উদাহরণ সংযুক্ত করা হলো।

---

## 1️⃣ **ভেরিয়েবল এবং ডাটা টাইপ**
```python
name = "Razu"  # String
i = 10  # Integer
f = 10.5  # Float
b = True  # Boolean
```

## 2️⃣ **শর্ত (If-Else)**
```python
x = 10
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")
```

## 3️⃣ **লুপ (For, While)**
### **For Loop:**
```python
for i in range(5):
    print(i)  # 0,1,2,3,4
```
### **While Loop:**
```python
i = 1
while i <= 5:
    print(i)
    i += 1
```

## 4️⃣ **ফাংশন (Functions)**
```python
def add(a, b):
    return a + b
print(add(5, 3))  # Output: 8
```

## 5️⃣ **Lambda Function**
```python
square = lambda x: x * x
print(square(4))  # Output: 16
```

## 6️⃣ **Yield & Generator**
```python
def generator_example(n):
    for i in range(n):
        yield i

for value in generator_example(5):
    print(value)  # 0,1,2,3,4
```

## 7️⃣ **OOP (Object-Oriented Programming)**
### **Class & Object:**
```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("Razu", 20)
print(student1.name, student1.age)
```

### **Encapsulation:**
```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private Variable

    def get_balance(self):
        return self.__balance
```

### **Inheritance:**
```python
class Vehicle:
    def move(self):
        print("Moving...")

class Car(Vehicle):
    def honk(self):
        print("Beep Beep!")

car = Car()
car.move()
car.honk()
```

### **Method Overriding & Super():**
```python
class Parent:
    def show(self):
        print("Parent Class")

class Child(Parent):
    def show(self):
        print("Child Class")
        super().show()

c = Child()
c.show()
```

### **Polymorphism:**
```python
class Bird:
    def fly(self):
        print("Birds can fly")

class Penguin(Bird):
    def fly(self):
        print("Penguins cannot fly")
```

### **Abstraction:**
```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Bark")
```

## 🔥 **শেষ কথা:**
এই পর্যন্ত যা শিখেছি, তা Python প্রোগ্রামিংয়ের বেসিক কভার করে। সামনে আরও ডিপ লেভেলে যাবো! 🚀
