# Exercises: Level 1
# Create an empty tuple
emp_tpl = ()
# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brothers = ("omkar", "rak", "manju")
sisters = ("sister1", "sister2", "sister3")

# Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters
print(siblings)

# How many siblings do you have?
print("length of the siblings", len(siblings))

# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = siblings + ("father", "mother")
print(family_members)

# Exercises: Level 2
# Unpack siblings and parents from family_members
sibling1, sibling2, sibling3, sibling4, sibling5, sibling6, father, mother = (
    family_members
)

all_siblings = (sibling1, sibling2, sibling3, sibling4, sibling5, sibling6)
parents = (father, mother)

print("All siblings: ", all_siblings)
print("Parents: ", parents)

# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ("apple", "banana", "orange", "grape", "strawberry")
vegetables = ("carrot", "broccoli", "spinach", "potato", "tomato")
animal_products = ("milk", "cheese", "eggs", "meat", "honey")

food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)

# Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
length = len(food_stuff_tp)
middle_index = length // 2

if length % 2 == 0:
    middle_items = food_stuff_lt[middle_index - 1 : middle_index + 1]
else:
    middle_items = food_stuff_lt[middle_index]

print("Middle item(s):", middle_items)

# Slice out the first three items and the last three items from food_stuff_lt list
first_three_items = food_stuff_lt[0:3]
last_three_items = food_stuff_lt[-3:]

print(first_three_items)
print(last_three_items)

# Delete the food_staff_tp tuple completely
del food_stuff_tp

# Check if an item exists in tuple:
print("apple" in fruits)

nordic_countries = ("Denmark", "Finland", "Iceland", "Norway", "Sweden")
# Check if 'Estonia' is a nordic country
print("Estonia" in nordic_countries)
# Check if 'Iceland' is a nordic country
print("Iceland" in nordic_countries)
