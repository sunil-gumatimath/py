# TUPLES IN PYTHON
# Tuples are ordered, immutable collections of items

# ============================
# 1. CREATING TUPLES
# ============================

# syntax
empty_tuple = ()
# or using the tuple constructor
empty_tuple = tuple()

# syntax
tpl = ('item1','item2','item3')
print(tpl)

fruits = ('banana','orange','mango','lemon')
print(fruits)

# Getting tuple length
tpl = ('item1','item2','item3')
print(len(tpl))

# ============================
# 2. ACCESSING TUPLE ELEMENTS
# ============================

# Syntax
tpl = ('item1', 'item2', 'item3')
first_item = tpl[0]
second_item = tpl[1]

print(first_item)
print(second_item)

fruits = ('banana','orange','mango','lemon')
first_fruit = fruits[0]
second_fruit = fruits[1]
last_index = len(fruits) - 1
last_fruit = fruits[last_index]

# Syntax
tpl = ('item1', 'item2', 'item3','item4')
first_item = tpl[-4]
second_item = tpl[-3]

print(first_fruit)
print(second_fruit)

fruits = ('banana', 'orange', 'mango', 'lemon')
first_fruit = fruits[-4]
second_fruit = fruits[-3]
last_fruit = fruits[-1]

print(first_fruit,second_fruit,last_fruit)

# ============================
# 3. SLICING TUPLES
# ============================

# Slicing tuples
# Syntax
tpl  = ('item1','item2','item3','item4')
all_items = tpl[0:4]
all_items = tpl[0:]
middle_two_items = tpl[1:3]

print(all_items)
print(middle_two_items)

fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[0:4]    # all items
all_fruits= fruits[0:]      # all items
orange_mango = fruits[1:3]  # doesn't include item at index 3
orange_to_the_rest = fruits[1:]

# Syntax
tpl = ('item1', 'item2', 'item3','item4')
all_items = tpl[-4:]         # all items
middle_two_items = tpl[-3:-1]  # does not include item at index 3 (-1)

fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[-4:]    # all items
orange_mango = fruits[-3:-1]  # doesn't include item at index 3
orange_to_the_rest = fruits[-3:]

# ============================
# 4. CONVERTING TUPLES TO LISTS
# ============================

# Chaining tuples to list
# Syntax
tpl = ('item1', 'item2', 'item3','item4')
lst = list(tpl)

fruits = ('banana', 'orange', 'mango', 'lemon')
fruits = list(fruits)
fruits[0] = 'apple'
print(fruits)     # ['apple', 'orange', 'mango', 'lemon']
fruits = tuple(fruits)
print(fruits)     # ('apple', 'orange', 'mango', 'lemon')

# ============================
# 5. CHECKING ITEMS IN TUPLES
# ============================

# Checking an Item in a Tuple
# Syntax
tpl = ('item1', 'item2', 'item3','item4')
'item2' in tpl # True

fruits = ('banana', 'orange', 'mango', 'lemon')
print('orange' in fruits) # True
print('apple' in fruits) # False
fruits[0] = 'apple' # TypeError: 'tuple' object does not support item assignment

# ============================
# 6. JOINING TUPLES
# ============================

# Joining Tuples
# syntax
tpl1 = ('item1', 'item2', 'item3')
tpl2 = ('item4', 'item5','item6')
tpl3 = tpl1 + tpl2

fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
fruits_and_vegetables = fruits + vegetables

# ============================
# 7. DELETING TUPLES
# ============================

# Deleting tuples
# syntax
tpl1 = ('item1', 'item2', 'item3')
del tpl1

fruits = ('banana', 'orange', 'mango', 'lemon')
del fruits
