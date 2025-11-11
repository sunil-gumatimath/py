# syntax
empty_tuple = ()
# or using the tuple constructor
empty_tuple = tuple()

# syntex
tpl = ('item1','item2','item3')
print(tpl)

fruits = ('banana','orange','mango','lemon')
print(fruits)

tpl = ('item1','item2','item3')
print(len(tpl))

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

# Slicing tuples

# Syntax
tpl  = ('item1','item2','item3','item4')
all_items = tpl[0:4]
all_items = tpl[0:]
middle_two_items = tpl[1:3]

print(all_items)
print(middle_two_items)