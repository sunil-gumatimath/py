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

for key, value in person.items():
    print(key, value)

# Loops in set
it_companies = {"Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"}
for company in it_companies:
    print(company)

# Break and Continue - Part 2
# Short reminder: Break: We use break when we like to stop our loop before it is completed.
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)
    if number == 3:
        break

# Continue: We use continue when we like to skip some of the steps in the iteration of the loop.
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print("Next number should be ", number + 1) if number != 5 else print("loop's end ")
print("Outside the loops")

# The Range Function

# The range() function is used list of numbers. The range(start, end, step) takes three parameters: starting, ending and increment.
# By default it starts from 0 and the increment is 1. The range sequence needs at least 1 argument (end). Creating sequences using range

lst = list(range(11))
print(lst)

st = set(range(1, 11))
print(st)

lst = list(range(0, 11, 2))
print(lst)
st = set(range(0, 11, 2))
print(st)

# syntax
# for iterator in range(start, end, step):

# Nested For Loop
# We can write loops inside a loop.

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
    if key == "skills":
        for skill in person["skills"]:
            print(skill)

# For Else
# If we want to execute some message when the loop ends, we use else.

# syntax
# for iterator in range(start, end, step):
#     do something
# else:
#     print('The loop ended')

for number in range(0, 11):
    print(number)
else:
    print("the loops end")

# Pass
# In python when statement is required (after semicolon), but we don't like to execute any code there, we can write the word pass to avoid errors.
# Also we can use it as a placeholder, for future statements.

for number in range(6):
    pass
