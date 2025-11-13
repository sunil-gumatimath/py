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

# Once a set is created we cannot change any items and we can also add additional items.
# Add one item using add()
st = {'item1', 'item2', 'item3', 'item4'}
st.add('item5')
print(st)

fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.add('apple')
print(fruits)

# Add multiple items using update() The update() allows to add multiple items to a set. The update() takes a list argument.
st = {'item1','item2','item3','item4'}
st.update(['item5','item6','item7'])

print(st)

fruits = {'apple','banana','orange','mango'}
vegetables = {'tomato','potato','cabbage','onion','carrot'}
fruits.update(vegetables)
print(fruits)

# Removing Items from a Set
st = {'item1','item2','item3','item4','item5'}
st.remove('item1')
print(st)

fruits = {'apple','banana','mango','orange'}
rm_fruit = fruits.pop()
# print('Removed Item :',rm_fruit)
print(fruits)

# Clearing Items in a Set
# If we want to clear or empty the set we use clear method.
st = {'item1','item2','item3','item4'}
print(st)
st.clear()
print(st)

# Deleting a Set
st = {'item1','item2','item3','item4'}
del st

fruits = {'banana', 'orange', 'mango', 'lemon'}
del fruits

# Converting 
lst = ['item1','item2','item3','item4','item1','item2']
st = set(lst)

print(st)
