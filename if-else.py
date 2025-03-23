# task 1
user_input = int(input("Enter Number: "))

if user_input > 0:
    print("This is a positive number.")
else:
    print("This is a negative number.")

# task 2
user_input = int(input("Enter your age: "))
if user_input >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# task 3
user_input = input("Enter multiple number: ")
my_list = user_input.split(",")
print(f"The largest number is {max(my_list)}")

# task 4
user_input = input("Enter multiple number: ")
if user_input == 'admin123':
    print("Access Granted")
else:
    print("Access Denied")

# task 5
user_input = int(input("Enter multiple number: "))
if user_input % 4 == 0:
    print(f"{user_input} is a Leap Year.")
else:
    print("Not Leap Year")


# task 1
user_input = int(input("Enter your number: "))
if user_input % 2 == 0:
    print("even")
else:
    print("odd")

# task 2
user_input = input("Enter your grade: ")
if user_input == 'A':
    print("Excellent")
elif user_input == 'B':
    print("Good")
elif user_input == 'C':
    print("Average")
elif user_input == 'D':
    print("Below Average")
elif user_input == 'F':
    print("Fail")
else:
    print('Not Match')

# task 3
first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
third = int(input("Enter third number: "))
large_num = max([first, second, third])


print(f"Large Number is", large_num)

# task 4
user_input = int(input("Enter leap year: "))

if user_input % 4 == 0 and user_input % 100 != 0 or user_input % 400 == 0:
    print(f"Leap year {user_input}")
else:
    print(f"Not Leap Year {user_input}")

# task 5
password = input("Enter password: ")
max_try = 3

if max_try > 3:
    print("Account Locked")
elif password == 'admin123':
    print("Access Granted")
else:
    max_try -= 1
    print(f"Account will lock after {max_try} times")

# Bonus task
first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
operator = input("Enter third number: ")
operators = ['+', '-', "*", '/']

if operator in operators:
    if operator == '+':
        print(f"{first+second}")
    elif operator == '-':
        print(f"{first-second}")
    elif operator == '*':
        print(f"{first*second}")
    elif operator == '/':
        print(f"{first/second}")
else:
    print("Operator Not Expcted")

