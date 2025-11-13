# TUPLES IN PYTHON
# Tuples are ordered, immutable collections of items

# ============================
# 1. CREATING TUPLES
# ============================

# Creating empty tuples
empty_tuple = ()
# or using the tuple constructor
empty_tuple = tuple()

# Creating tuples with items
tpl = ('item1', 'item2', 'item3')
print(tpl)

fruits = ('banana', 'orange', 'mango', 'lemon')
print(fruits)

# Getting tuple length
tpl = ('item1', 'item2', 'item3')
print(len(tpl))

# ============================
# 2. ACCESSING TUPLE ELEMENTS
# ============================

# Positive indexing
tpl = ('item1', 'item2', 'item3')
first_item = tpl[0]
second_item = tpl[1]

print(first_item)
print(second_item)

fruits = ('banana', 'orange', 'mango', 'lemon')
first_fruit = fruits[0]
second_fruit = fruits[1]
last_index = len(fruits) - 1
last_fruit = fruits[last_index]

print(first_fruit)
print(second_fruit)
print(last_fruit)

# Negative indexing
tpl = ('item1', 'item2', 'item3', 'item4')
first_item = tpl[-4]
second_item = tpl[-3]

print(first_item)
print(second_item)

fruits = ('banana', 'orange', 'mango', 'lemon')
first_fruit = fruits[-4]
second_fruit = fruits[-3]
last_fruit = fruits[-1]

print(first_fruit, second_fruit, last_fruit)

# Tuple methods: count and index
fruits = ('apple', 'banana', 'apple', 'orange', 'apple')
print(fruits.count('apple'))

# Returns the index of the first occurrence of a value
fruits = ('apple', 'banana', 'apple', 'orange')
print(fruits.index('apple'))  # Output: 0 (first occurrence)
print(fruits.index('orange')) # Output: 3

# ============================
# 3. SLICING TUPLES
# ============================

# Slicing tuples
tpl = ('item1', 'item2', 'item3', 'item4')
all_items = tpl[0:4]
print(all_items)
all_items = tpl[0:]
print(all_items)
middle_two_items = tpl[1:3]
print(middle_two_items)

fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[0:4]    # all items
print(all_fruits)
all_fruits = fruits[0:]      # all items
print(all_fruits)
orange_mango = fruits[1:3]  # doesn't include item at index 3
print(orange_mango)
orange_to_the_rest = fruits[1:]
print(orange_to_the_rest)

# Negative slicing
tpl = ('item1', 'item2', 'item3', 'item4')
all_items = tpl[-4:]         # all items
print(all_items)
middle_two_items = tpl[-3:-1]  # does not include item at index 3 (-1)
print(middle_two_items)

fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[-4:]    # all items
print(all_fruits)
orange_mango = fruits[-3:-1]  # doesn't include item at index 3
print(orange_mango)
orange_to_the_rest = fruits[-3:]
print(orange_to_the_rest)

# ============================
# 4. CONVERTING TUPLES TO LISTS
# ============================

# Converting tuples to lists for modification
tpl = ('item1', 'item2', 'item3', 'item4')
lst = list(tpl)
print(lst)

fruits = ('banana', 'orange', 'mango', 'lemon')
fruits_list = list(fruits)
fruits_list[0] = 'apple'
print(fruits_list)     # ['apple', 'orange', 'mango', 'lemon']
fruits_tuple = tuple(fruits_list)
print(fruits_tuple)     # ('apple', 'orange', 'mango', 'lemon')

# ============================
# 5. CHECKING ITEMS IN TUPLES
# ============================

# Checking an Item in a Tuple
tpl = ('item1', 'item2', 'item3', 'item4')
print('item2' in tpl) # True

fruits = ('banana', 'orange', 'mango', 'lemon')
print('orange' in fruits) # True
print('apple' in fruits) # False

# Tuples are immutable - this will raise an error
try:
    fruits[0] = 'apple'
except TypeError as e:
    print(f"TypeError: {e}")

# ============================
# 6. JOINING TUPLES
# ============================

# Joining Tuples
tpl1 = ('item1', 'item2', 'item3')
tpl2 = ('item4', 'item5', 'item6')
tpl3 = tpl1 + tpl2
print(tpl3)

fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot')
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)

# ============================
# 7. DELETING TUPLES
# ============================

# Deleting tuples
tpl1 = ('item1', 'item2', 'item3')
print("Before deletion:", tpl1)
del tpl1
# print(tpl1)  # This would raise NameError

fruits = ('banana', 'orange', 'mango', 'lemon')
print("Before deletion:", fruits)
del fruits
# print(fruits)  # This would raise NameError
