# task 1
num = input("Enter number: ")
sum = sum(int(i) for i in num)
print(sum)

# task 2
task2 = input("Enter Armstrong number: ")
digits = [pow(int(d), 3) for d in task2]
task2Sum = sum(digits)

if(int(task2) == task2Sum):
    print("Armstrong Number")
else:
    print("Not Armstrong Number")

# task 3
num = input("Enter a number: ")
digits = num[::-1]
print(digits)

# task 4
num = int(input("Enter a number: "))

def find_factor(x):
    for i in range(1, x + 1):
        if x % i == 0:
           print("Factors", i)

find_factor(num)

# task 5
num = input("Enter a number: ")
output = int(num[::-1])

if(int(num) == output):
    print("Yes, it's a Palindrome!  ")
else:
    print("No, it's not a Palindrome.  ")