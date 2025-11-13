# We use the set() built-in function.
from turtle import reset
from unittest import result


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

fruits = {'apple','banana','orange','mango','banana','lemon','apple'}
st = set(fruits)
print(st)

# Joining sets
# We can join two sets using the union() or update() method.
st1 = {'item1','item2','item4','item6'}
st2 = {'item5','item6','item3','item2'}
st3 = st1.union(st2)
print(st3)

fruits = {'banana','apple','orange','lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
print(fruits.union(vegetables))

# Update This method inserts a set into a given set
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st1.update(st2) # st2 contents are added to st1
print(st1)

fruits = {'banana','apple','orange','lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
fruits.update(vegetables)
print(fruits)

# Finding Intersection Items
# Intersection returns a set of items which are in both the sets. See the example
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2'}
st3=st1.intersection(st2) # {'item3', 'item2'}
print(st3)

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
result = whole_numbers.intersection(even_numbers) # {0, 2, 4, 6, 8, 10}
print(result)

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
result = python.intersection(dragon)     # {'o', 'n'}
print(result)
