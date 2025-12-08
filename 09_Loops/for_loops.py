# for loops
# A for loop is a control structure that iterates over an iterable (e.g., list, tuple, string, range), executing a code block for each element.

# syntax
# for iterator in lst:
#     code goes here

numbers = [0, 1, 2, 3, 4, 5]
for number in numbers:
    print(number)

items = ["item1", "item2", "item3", "item4"]
for item in items:
    print(item)

# For loop with string
language = "Pyhton"
for letter in language:
    print(letter)

for i in range(len(language)):
    print(language[i])

# For loop with tuple
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)

# For loop with dictionary Looping through a dictionary gives you the key of the dictionary.
person = {
    "first_name": "luffy",
    "last_name": "nika",
    "age": 24,
    "country": "OnePiece",
    "is_married": False,
    "skills": ["gear1", "gear2", "gear3", "gear4"],
    "address": {"stree": "BTM", "city": "BNG"},
}

for key in person:
    print(key)
    
for key,value in person.items():
    print(key,value)
    
# Loops in set
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    print(company)

# Break and Continue - Part 2
# Short reminder: Break: We use break when we like to stop our loop before it is completed.
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        break