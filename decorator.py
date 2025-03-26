def decorator(func):
    def wrapper():
        print("Before call func")
        func()
        print("After call function")
    return wrapper

@decorator
def say_hello():
    print("hello")

say_hello()


def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello {name}")

greet('Razu')

class Logger:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwds):
        print(f"Calling function: {self.func.__name__}")
        return self.func(*args, **kwds)

@Logger
def add(a, b):
    return a + b

print(add(10,5))

# task 1

def app_decorator(func):
    def wrapper():
        print("Function is being called... ")
        func()
        print("Function execution finished! ")
    return wrapper

@app_decorator
def test():
    print('hello')
test()

# task 2

def make_square(func):
    def wrapper():
        result = func()
        return result ** 2
    return wrapper

@make_square
def get_number():
    return 5

print(get_number()) 

# task 3
import time
def timeCount(func):
    def wrapper():
        start = time.perf_counter()
        func()
        end = time.perf_counter()
        print(f"Execution time: {end - start:.6f} seconds")
    return wrapper

@timeCount
def add():
    print("run")
add()

# task 4

def uppercase(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

def exclaim(func):
    def wrapper():
        result = func()
        return result + '!!!'
    return wrapper

@exclaim
@uppercase
def hello():
    return "hello"

print(hello())  

# task 5
class Logger:
    def __init__(self, func):
        self.func = func
    def __call__(self, *args, **kwds):
        print('Calling function...')
        return self.func(*args, **kwds)

@Logger
def call_func():
    print("hello")

call_func()

# Bonus Task
def log_function_call(func):
    def wrapper(*args, **kwargs):
        result  = func(*args, **kwargs)
        print(f"Function name: {func.__name__}")
        print(f"Arguments: {args}, Keyword Arguments: {kwargs}")
        return result
    return wrapper

@log_function_call
def call_with_args(a,b):
    return a ** b

print(call_with_args(10,20))