# We use the set() built-in function.
st = set()
print(st)
print(type(st))

# syntax
st = {'item1', 'item2', 'item3', 'item4'}
print(st)

# syntax
fruits = {'banana', 'orange', 'mango', 'lemon'}
print(fruits)


# We use len() method to find the length of a set.
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
len(st)

fruits = {'banana', 'orange', 'mango', 'lemon'}
print(len(fruits))

# Checking an Item
# To check if an item exist in a list we use in membership operator.
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
print("Does set st conatin item 3 : ", 'item3' in st) # Does set st contain item3? True

fruits = {'banana', 'orange', 'mango', 'lemon'}
print('mango' in fruits)        # True
