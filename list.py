# items = ['first', 'second','third', 'four', 'give']
# print(items[1])
# items.append("new item")
# print(items[0:3])
# print(len(items))


# task 1
# numList = [1,2,3,4,5]
# print(numList[0])
# print(numList[-1])
# numList.append(6)
# print(numList)

# task 2
# strList =  ['first', 'second', 'third', 'four', 'five']
# print(strList[::-1])
# strList.sort()
# print(strList)

# task 3
# strList =  ['first', 'second', 'third', 'four', 'five']
# strList.remove('four')
# print(strList)

# task 4
# numList = [1,2,3,4,5]
# print(sum(numList))
# print(max(numList))
# print(min(numList))

# task 5
# dupList = [1,2,3,4,5,5,6,6]
# newList = []

# for item in dupList:
#     if item in newList:
#         continue
#     else:
#         newList.append(item)

# print(newList)

# task 1
# evenNumbersLists = [x for x in range(20) if x % 3 == 0]
# print(evenNumbersLists)

# task 2
# strLists = ['apple', 'comla', 'malta']
# upperLists = [item.upper() for item in strLists]
#     print(upperLists)

# task 3
# sqLists = [x**2 for x in range(20)]
# print(sqLists)

# task 4
# numList = [1,2,3,-4,-5,-6]
# positiveNum = [x for x in numList if x > 0]
# print(positiveNum)

# task 5
# sentence = 'Python programming is really fun and powerful'
# sen_length = [len(x) for x in sentence.split(" ")]
# print(sen_length)

# task 1
# my_list = []
# for x in range(5):
#     num = int(input("Enter Number: "))
#     my_list.append(num)

# my_list.pop()
# print(my_list)

# task 2
# names_list = ['razu', 'rakib', 'hasan', 'sumon']
# user_input = input("Enter your name: ")

# if(user_input in names_list):
#     print("Your Name is", names_list.index(user_input))
# else:
#     print("Not match")

# task 3
# import math
# num_lists = [2, 3, 4, 5]
# print(math.prod(num_lists))

# task 4
# num_lists = [2, 3, 4, 5]
# new_evn = [x for x in num_lists if x % 2 == 0]
# print(new_evn)

# task 5
# user_input = input("Enter a sentence: ")
# count_sen = [len(x) for x in user_input.split(" ")]
# print(count_sen)

# task 1
# user_list = []

# for ask in range(5):
#     user_input = input("Enter your number: ")
#     user_list.append(user_input)

# user_list.sort()
# print(user_list)

# task 2
# numbers = [10, 20, 30, 40, 50]
# user_input = int(input("Enter a number: "))
# numbers.insert(2, user_input)
# print(numbers)

# task 3
# words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
# print(words.count('apple'))

# task 4
# numbers = [10, 20, 30, 40, 50]
# numbers.remove(int(input("Remove your number: ")))
# numbers.pop()
# print(numbers)

# task 5
# nums = [5, 1, 8, 3, 6]
# nums.sort(reverse=True)
# print(nums)

# task Bonus
# nums = [1,2,3]
# nums.extend([4,5,6])
# print(nums)