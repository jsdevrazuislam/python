# task 1
test_dict = {
    'food_name': 'test',
    'color': 'red',
    'language': 'english'
}


test_dict['city'] = 'pabna'
test_dict['color'] = 'blue'

del test_dict['color']

print(test_dict.keys())
print(test_dict.values())
print(test_dict.items())
print(test_dict.get('food_name'))
test_dict.update({ 'color': 'danger', 'language': 'bangla'})
test_dict.pop('color')
test_dict.popitem()
test_dict.clear()
print(test_dict)
for key, value in test_dict.items():
    print('key and value', key, value)


# task 1
student = {
    'name':"Razu Islam",
    'age':20,
    'subject_list': ['bangla', 'english', 'math']
}

print(student.keys())
print(student.values())

# task 2
fruits = {
    'apple': 200,
    'orange': 400,
    'banana': 500,
    'stroberi': 600
}

user_input = input("Enter fruit name: ")

if user_input in fruits.keys():
    print("Your Food Price is", fruits[user_input])
else:
    print("Sorry, this fruit is not available!")

# task 3

countries = {
    'Bangladesh': 'Dhaka',
    'India': 'Delhi',
    'Japan':'Tokyo'
}

user_input = input("Enter your country name: ")

if user_input in countries.keys():
    print("The capital of {name} is {raj}.".format(name=user_input, raj=countries[user_input]))
else:
    print("Country not found!")

# task 5

fruits = {
    'apple': 200,
    'orange': 400,
    'banana': 500,
    'stroberi': 600
}

user_input = input("Enter product name: ")

if user_input in fruits.keys():
    value = fruits.get(user_input)
    fruits.update({ user_input: value - 1})
else:
    print("Out of stock!")

print(fruits)

# task1 
store_dict = {
    'name':'razu islam',
    'age': 20,
    'city': 'pabna',
    'fav_food': 'apple'
}

print(store_dict.get('city'), store_dict.get('fav_food'))

# task 4
temp_city = {
    'pabna': 3.5,
    'dhaka': 40,
    'rajshahi': 50
}

def find_temp_in_city(city):
    for key, value in temp_city.items():
        if city == key:
            print(value)
            break
        else:
            print("City not found!")
            break


find_temp_in_city(input("Enter city name: "))

# # task 5
currency_informations = {
    'dhaka': 'BDT',
    'delhi': 'Rupi',
    'california':'Dollar'
}

def fine_currency(city):
    for key, value in currency_informations.items():
        if city == key:
            print("City {city} and currency {tk}".format(city=key, tk=value))
            break
        else:
            print("Not Found")
            break

fine_currency(input("Enter city name: "))

