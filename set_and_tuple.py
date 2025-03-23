# task 1
my_tuple = (-5, 10, -2, 7, -1, 9)
positive_sum = []
for item in my_tuple:
    if item > 0:
        positive_sum.append(item)

print(sum(positive_sum))

# task 2
my_set = {3, 5, 7, 9, 11}
my_set.add(12)
my_set.remove(3)
print(len(my_set))

# task 3
my_tuple = (12, 15, 20, 25, 30)
total = sum(my_tuple)
print(total / len(my_tuple))

# # task 4
my_set = {1, 2, 3, 4, 5}
my_tuple = (10, 20, 30)

num_to_check = int(input("Enter a number to check in set: "))

if num_to_check in my_set:
    my_tuple = my_tuple + (num_to_check,) 
    print("Updated Tuple:", my_tuple)
else:
    print("Number not found in set. Tuple remains the same:", my_tuple)


# task 5
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1.intersection(set2))

# task 6
my_tuple = (5, 12, 8, 15, 2, 19)
my_list = []

for item in my_tuple:
    if item > 10:
        my_list.append(item)

print(my_list)

# task 7
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

print(set1.difference(set2))



# task 1
numbers = (1,2,3,4,5,6,7,8)
new_list = [x for x in numbers if x % 2 == 0]
print(new_list)

# task 2
set1 = {2, 4, 6, 8, 10}
set2 = {5, 6, 7, 8, 9}

print(set1.symmetric_difference(set2))

# task 3
words = ("apple", "banana", "cherry", "date", "fig", "grape")

for char in words:
    if len(char) >= 5:
        print(char)

# # task 4
numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
numbers = {x for x in numbers if x % 3 != 0} 
print(numbers)

# task 5
nums = (4, 7, 2, 8, 10, 3, 5, 9)
print(max(nums))
print(min(nums))

# bonus task
set_numbers = {5, 10, 15, 20}
tuple_numbers = (10, 20, 30, 40)

print(set_numbers.intersection(tuple_numbers))