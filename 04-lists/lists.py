empty_list: list[int] = []
print(len(empty_list))

fruits = ['banana', 'orange', 'mango', 'lemon']                         # list of fruits
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']          # list of vegetables
animal_products = ['milk', 'meat', 'butter', 'yoghurt']                 # list of animal products
web_techs = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB']    # list of web technologies
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
print(last_fruit)       # lemon
print(second_last)      # mango