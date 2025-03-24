def first_func():
    print("Hello Python to run this fun")

first_func()

def second_func(name):
    print(f"Hello Mr {name}")

second_func("Razu")

def third_func(name='Guest'):
    print(f"Hello Mr {name}")

third_func("Ali")
third_func()

def four_func(a,b):
    return a + b
print(four_func(20, 30))

def five_func(*args):
    return sum(args)
print(five_func(100,200,400,400))

def six_func(**args):
    for key, item in args.items():
        print(f"{key} {item}")
print(six_func(name='Razu Islam', age=20, title='Engineer'))

square = lambda x: x * x
print(square(100))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))


# task 1
def square(n):
    return  n * n

print(square(5))

# task 2
def return_sum_list(list):
    return sum(list)
print(return_sum_list([1, 2, 3, 4, 5]))

# task 3
def slice_str(str):
    return f"{str[0]}{str[-1]}"

print(slice_str('hello'))

# task 4
def is_prime_number(num):
    if num < 2:
        return "Not Prime Number"
    
    for i in range(2, int(num ** 0.5) + 1):  
        if num % i == 0:
            return "Not Prime Number"
    return "Prime Number"

print(is_prime_number(2))
print(is_prime_number(4)) 
print(is_prime_number(13))


# task 5
def find_even(list):
    result = []
    for item in list:
        if item % 2 == 0:
            result.append(item) 
    return result

print(find_even([10, 15, 20, 25, 30]))

# task 6
def multiply(x,y=2):
    return x * y
print(multiply(5,3))
print(multiply(7))

# task 7
def find_big_number(list):
    return max(list)
print(find_big_number([12, 45, 78, 34, 90]))

# task 8
def multiples(number, count):
    for i in range(1, count + 1):
        yield number * i 

for value in multiples(3, 5):
    print(value)


# task 9
def sen_count(str):
    return len(str.split(" "))

print(sen_count("Python is awesome"))

#  Bonus Task
def find_unique_list(list):
    new_list = []
    for x in list:
        if x in new_list:
            continue
        else:
            new_list.append(x)
    return new_list

print(find_unique_list([1, 2, 2, 3, 4, 4, 5]))

# task 1

def odd_numbers(n):
    for x in range(n):
        yield x * 2 + 1

for item in odd_numbers(7):
    print(item)

# task 2
def fibonacci_series(n):
    a,b = 0,1
    for _ in range(n):
        yield a
        a,b = b, a + b

for x in fibonacci_series(6):
    print(x)

# task 3
def factorial_gen(n):
    result = 1
    for x in range(1, n + 1):
        result *= x
        yield result

for x in factorial_gen(5):
    print(x)


# task 1
def task(n):
    result = 1
    for x in range(1, n + 1):
            if x % 2 != 0:
                yield result
                result = (result + 2) + x

for x in task(7):
    print(x)

