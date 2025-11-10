# Python Lists Tutorial
# This script demonstrates various operations on Python lists

# Section 1: Creating Lists
empty_list: list[int] = []
print('Length of empty list:', len(empty_list))

fruits = ['banana', 'orange', 'mango', 'lemon']  # list of fruits
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']  # list of vegetables
animal_products = ['milk', 'meat', 'butter', 'yoghurt']  # list of animal products
web_techs = ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'MongoDB']  # list of web technologies
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']

# Section 2: Printing Lists and Their Lengths
print('Fruits:', fruits)
print('Number of fruits:', len(fruits))
print('Vegetables:', vegetables)
print('Number of vegetables:', len(vegetables))
print('Animal products:', animal_products)
print('Number of animal products:', len(animal_products))
print('Web technologies:', web_techs)
print('Number of web technologies:', len(web_techs))
print('Number of countries:', len(countries))
print()

# Section 3: Accessing List Items
fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits[0]
print('First fruit:', first_fruit)
second_fruit = fruits[1]
print('Second fruit:', second_fruit)
last_fruit = fruits[-1]
print('Last fruit:', last_fruit)

# Last index
last_index = len(fruits) - 1
print('Last index:', last_index)
print()

# Section 4: Slicing Lists
fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[0:4]
print('All fruits:', all_fruits)

# This gives the same result
all_fruits = fruits[0:]  # if we don't set where to stop it takes all the rest
print('All fruits (alternative):', all_fruits)

orange_and_mango = fruits[1:3]  # it does not include the end index
print('Orange and mango:', orange_and_mango)

orange_mango_lemon = fruits[1:]
print('Orange, mango, lemon:', orange_mango_lemon)

# Using negative indices
all_fruits = fruits[-4:]  # it returns all the fruits
print('All fruits (negative index):', all_fruits)

orange_and_mango = fruits[-3:-1]  # it does not include the end index
print('Orange and mango (negative):', orange_and_mango)

orange_mango_lemon = fruits[-3:]
print('Orange, mango, lemon (negative):', orange_mango_lemon)

# Section 5: Modifying List Items
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits[0] = 'avocado'
print('After changing first fruit:', fruits)

fruits[1] = 'apple'
print('After changing second fruit:', fruits)

last_index = len(fruits) - 1
fruits[last_index] = 'lime'
print('After changing last fruit (by index):', fruits)

fruits[-1] = 'lime'
print('After changing last fruit (negative index):', fruits)

# Section 6: Checking if an Item Exists in a List
fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits
print('Does banana exist in fruits?', does_exist)  # True

does_exist = 'lime' in fruits
print('Does lime exist in fruits?', does_exist)  # False

# Section 7: Adding Items to a List
# Append
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.append('apple')
print('After appending apple:', fruits)

fruits.append('lime')
print('After appending lime:', fruits)

# Insert
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(1, 'apple')  # insert apple between banana and orange
print('After inserting apple at index 1:', fruits)

fruits.insert(3, 'lime')  # insert lime at index 3
print('After inserting lime at index 3:', fruits)

# Section 8: Removing Items from a List
# Remove
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.remove('banana')
print('After removing banana:', fruits)

fruits.remove('lemon')
print('After removing lemon:', fruits)

# Pop
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.pop()  # removes the last item
print('After popping last item:', fruits)

fruits.pop(0)  # pop based on index
print('After popping first item:', fruits)

# Del
fruits = ['banana', 'orange', 'mango', 'lemon']
del fruits[0]
print('After deleting first item:', fruits)

del fruits[1]
print('After deleting second item:', fruits)

del fruits
print(fruits)     # NameError: name 'fruits' is not defined

# Clear
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.clear()
print('After clearing the list:', fruits)

# Section 9: Copying a List
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_copy = fruits.copy()
print('Copied list:', fruits_copy)

fruits_copy_1 = fruits[:]
print('Copied list (slicing):', fruits_copy_1)

# Section 10: Joining Lists
# Using concatenation
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers = [-5, -4, -3, -2, -1]
integers = positive_numbers + zero + negative_numbers
print('Joined integers:', integers)

fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits_and_vegetables = fruits + vegetables
print('Fruits and vegetables:', fruits_and_vegetables)

# Using extend
num1 = [0, 1, 2, 3]
num2 = [4, 5, 6]
num1.extend(num2)
print('Numbers after extend:', num1)

negative_numbers = [-5, -4, -3, -2, -1]
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]

negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)
print('Integers after extend:', negative_numbers)

fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits.extend(vegetables)
print('Fruits and vegetables after extend:', fruits)

# Section 11: Counting Items in a List
fruits = ['banana', 'orange', 'mango', 'lemon']
print('Count of orange in fruits:', fruits.count('orange'))

ages = [22, 19, 24, 25, 26, 24, 25, 24]
print('Count of 24 in ages:', ages.count(24))

# Section 12: Finding Index of an Item
fruits = ['banana', 'orange', 'mango', 'lemon']
print('Index of mango in fruits:', fruits.index('mango'))

ages = [22, 19, 24, 25, 26, 24, 25, 24]
print('Index of 25 in ages:', ages.index(25))

# Section 13: Reversing a List
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.reverse()
print('Reversed fruits:', fruits)

ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.reverse()
print('Reversed ages:', ages)

# Section 14: Sorting List Items
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.sort()
print('Sorted fruits (ascending):', fruits)

fruits.sort(reverse=True)
print('Sorted fruits (descending):', fruits)

ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.sort()
print('Sorted ages (ascending):', ages)

ages.sort(reverse=True)
print('Sorted ages (descending):', ages)
