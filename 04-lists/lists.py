empty_list: list[int] = []
print(len(empty_list))

fruits = ['banana', 'orange', 'mango', 'lemon']                         # list of fruits
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']          # list of vegetables
animal_products = ['milk', 'meat', 'butter', 'yoghurt']                 # list of animal products
web_techs = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongoDB']    # list of web technologies
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']

# Print the lists and it length
print('Fruits:', fruits)
print('Number of fruits:', len(fruits))
print('Vegetables:', vegetables)
print('Number of vegetables:', len(vegetables))
print('Animal products:',animal_products)
print('Number of animal products:', len(animal_products))
print('Web technologies:', web_techs)
print('Number of web technologies:', len(web_techs))
print('Number of countries:', len(countries))
print('')


# Modifying list
fruits = ['banana','orange','mango','lemon']
first_fruit = fruits[0]
print(first_fruit)
second_fruit = fruits[1]
print(second_fruit)
last_fruit = fruits[-1]
print(last_fruit)

# Last index
last_index = len(fruits) - 1
print(last_index)

print(' ')

# Accessing items
fruits = ['banana', 'orange', 'mango', 'lemon'] 
last_fruit = fruits[-1]
second_last = fruits[-2]
print(last_fruit)                                                          # lemon
print(second_last)                                                         # mango

# Slicing items
fruits = ['banana', 'orange', 'mango', 'lemon'] 
all_fruits = fruits[0:4]
print(all_fruits)
# this is also give the same result as the above
all_fruits = fruits[0:]                                                      # if we don't set where to stop it takes all the rest
print(all_fruits)
orange_and_mango = fruits[1:3]                                               # it does not include the end index
orange_mango_lemon = fruits[1:]
print(orange_and_mango)
print(orange_mango_lemon)

fruits = ['banana', 'orange', 'mango', 'lemon'] 
all_fruits = fruits[-4:]                                                     # it returns all the fruits
# this is also give the same result as the above
orange_and_mango = fruits[-3:-1]                                             # it does not include the end index
orange_mango_lemon = fruits[-3:]

fruits = ['banana', 'orange', 'mango', 'lemon'] 
fruits[0] = 'avocada'
print(fruits)
fruits[1] = 'apple'
print(fruits)

last_index = len(fruits) - 1
fruits[last_index] = 'lime'
print(fruits)

fruits[-1] = 'lime'
print(fruits)

# checking items
fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits
print(does_exist)                                                           # True
does_exist = 'lime' in fruits
print(does_exist)                                                           # False

# append
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.append('apple')                                                      # ['banana', 'orange', 'mango', 'lemon', 'apple']
print(fruits)
fruits.append('lime')                                                       # ['banana', 'orange', 'mango', 'lemon', 'apple', 'lime]
print(fruits)

# insert
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(1,'apple')                                                    # insert apple between banana and orange
print(fruits)                                                               # ['banana', 'apple', 'orange', 'mango', 'lemon']
fruits.insert(3,'lime')                                                     # ['banana', 'apple', 'orange', 'lime', 'mango', 'lemon']
print(fruits)

# remove
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.remove('banana')
print(fruits)                                                               # ['orange', 'mango', 'lemon']
fruits.remove('lemon')
print(fruits)                                                               # ['orange', 'mango']

# pop 
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.pop()
print(fruits)                                                               # ['banana', 'orange', 'mango']
# we can pop based on the index too
fruits.pop(0)
print(fruits)                                                               # ['orange', 'mango'] 

# del
fruits = ['banana', 'orange', 'mango', 'lemon']
del fruits[0]
print(fruits)                                                                 # ['orange', 'mango', 'lemon']

del fruits[1]
print(fruits)                                                                 # ['orange', 'lemon']

del fruits
print(fruits)                                                                 # NameError: name 'fruits' is not defined

# clear
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.clear()
print(fruits)

# copying a lists
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_copy = fruits.copy()
fruits_copy_1 = fruits_copy[:]
print(fruits_copy)            
print(fruits_copy_1)                                                  # ['banana', 'orange', 'mango', 'lemon']

#  join
positive_numbers = [1,2,3,4,5]
zero = [0]
negative_numbers = [-5,-4,-3,-2,-1]
integers = positive_numbers + zero + negative_numbers
print(integers)                                                        # [1, 2, 3, 4, 5, 0, -5, -4, -3, -2, -1]

fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot'] 
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)                                           # ['banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']

# join with extend
num1 = [0,1,2,3]
num2 = [4,5,6]
num1.extend(num2)                                                        # Number : [0, 1, 2, 3, 4, 5, 6]
print('Number :',num1)                      

negative_numbers = [-5,-4,-3,-2,-1]
positive_numbers = [1, 2, 3,4,5]
zero = [0]

negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)                               # Integers :  [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
print('Integers : ',negative_numbers)

fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
fruits.extend(vegetables)
print('Fruits and vegetables:', fruits)                                 # Fruits and vegetables: ['banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']

# count
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.count('orange'))

ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))

# index
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.index('mango'))

ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.index(25))

# Reverse
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.reverse()
print(fruits)
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.reverse()
print(ages)

# sort
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)

ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.sort()
print(ages) 
ages.sort(reverse=True)
print(ages) 