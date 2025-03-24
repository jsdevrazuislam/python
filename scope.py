# task 1
count = 0

def increment_count():
    global count
    count += 1

increment_count()
increment_count()
print(count)

# task 2
def outer_function():
    def inner():
        print("I am inside the inner function!")
    inner()

outer_function()

# task 3
def create_counter():
    count = 0
    def inner():
        nonlocal count  
        count += 1
        return count
    return inner

counter = create_counter()
print(counter())  
print(counter())  
print(counter())  

# task 4
def multiplier(n):
    def inner(x):
        return n * x
    return inner

multiply_by_5 = multiplier(5)
print(multiply_by_5(2))
print(multiply_by_5(3))
print(multiply_by_5(4))

# task 5
def add(x,y):
    def inner():
        return x + y
    return inner

add_numbers = add(10, 20)
print(add_numbers())  
