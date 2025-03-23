# task 1
for item in range(10):
    if item == 7:
        print(f"Got value {item}")
        break
# task 2

i = 1

while i <= 10:
    if i == 3 or i == 6:
        i += 1
        continue
    else:
        print(i)
    i += 1

# task 3

i = 1
while i <= 10:
    print(i)
    i += 1
else:
    print("Loop completed!")

# task 4
my_list = ['apple', 'banana', 'grape', 'mango']

for item, index in enumerate(my_list):
    print(f"{index} {item}")

# task 5
for item in range(20):
    if item == 15:
        print("15 is found, breaking loop!")
        break
else:
    print("Loop completed without break!")

# task 6
for item in range(1, 10):
    if item % 4 == 0:
        continue
    print(item)
else:
    print("No 4's multiples were skipped.")