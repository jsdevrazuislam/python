# task 1
string = input("Enter a string: ")
for str in string:
    print(str)

# task 3
string = input("Enter a string: ") 
vowels = "aeiouAEIOU"

for char in  string:
    if char in vowels:
        print(char)

# task 2
string = input("Enter a string: ")
print("Reversed string: ", string[::-1])

# task 4
string = input("Enter a string: ")
print("Length of string: ", string.__len__())

# task 5
string = input("Enter a string: ")

if(string[0] == string[-1]):
    print("Yes, first and last letters are the same!  ")
else:
    print("No, first and last letters are different.  ")

# task 1
string = input("Enter a string: ")
vowels = "aeiouAEIOU"

found_consonants = []

for char in string:
    if char in vowels:
        continue
    else:
        found_consonants.append(char)

print("Consonants:", ", ".join(found_consonants))  

# task 2
string = input("Enter a string:  ")
vowels = "aeiouAEIOU"

found_vowel = []

for char in string:
    if char in vowels:
        found_vowel.append(char)
print(found_vowel.__len__())

# task 3
string = input("Enter a sentence: ")
space = ' '
found_space = []

for char in string:
    if char in space:
        found_space.append(char)

print("Total spaces: ", found_space.__len__())

# task 4
string = input("Enter a string: ")
max_count = 0
max_char = ''

for char in string:
    count = string.count(char)
    if count > max_count: 
        max_count = count
        max_char = char
print(f"Most frequent letter: {max_char}")

# task 5
string = input("Enter a sentence: ")
cap_sen = ''

for char in string.split(" "):
    cap_sen += char + " "

print("Capitalized sentence: ", cap_sen.capitalize())
