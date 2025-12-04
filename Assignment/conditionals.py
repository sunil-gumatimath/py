# Exercises: Level 1
# Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive.
# If below 18 give feedback to wait for the missing amount of years. Output:

age = int(input("Enter your age: "))

if age >= 18:
    print("You are old enough to drive.")
else:
    years_needed = 18 - age
    print(f"You need {years_needed} more years to drive.")


# Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input.
# You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:

my_age = 25

your_age = int(input("Enter your age: "))

if my_age > your_age:
    diff = my_age - your_age
    if diff == 1:
        print("I am 1 year older than you.")
    else:
        print(f"I am {diff} years older than you.")
elif your_age > my_age:
    diff = your_age - my_age
    if diff == 1:
        print("You are 1 year older than me.")
    else:
        print(f"You are {diff} years older than me.")
else:
    print("We are the same age.")

# Get two numbers from the user using input prompt. If a is greater than b return a is greater than b,
# if a is less b return a is smaller than b, else a is equal to b. Output:

num_1 = int(input("Enter number one: "))
num_2 = int(input("Enter number two: "))

if num_1 > num_2:
    print(f'{num_1} is greater than {num_2}')
elif num_2 > num_1:
    print(f'{num_2} is greater than {num_1}')
else:
    print(f'{num_1} is equal to {num_2}')

# Exercises: Level 2
# Write a code which gives grade to students according to theirs scores:

marks = int(input("Enter the percentage: "))

if marks >= 80 and marks <= 100:
    print("Grade A")
elif marks >= 70 and marks <= 79:
    print("Grade B")
elif marks >= 60 and marks <= 69:
    print("Grade C")
elif marks >= 50 and marks <= 59:
    print("Grade D")
elif marks >= 0 and marks <= 49:
    print("failed")

# Check if the season is Autumn, Winter, Spring or Summer. If the user input is:
# September, October or November, the season is Autumn. December, January or February, the season is Winter.
# March, April or May,the season is Spring June, July or August, the season is Summer

month = input('Enter the month: ')

if month == "September" or month == "October" or month == "November":
    print('Autumn')
elif month == "December" or month == "January" or month == "February":
    print('Winter')
elif month == "March" or month == "April" or month == "May":
    print('Spring')
elif month == "June" or month == "July" or month == "August":
    print('Summer')
else:
    print('invalid input')

# The following list contains some fruits:
# fruits = ['banana', 'orange', 'mango', 'lemon']
# If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')

fruits = ["banana", "orange", "mango", "lemon"]
appended_fruit = None  # Variable to store the appended value for later use

fruit = input("Enter the fruit: ")

if fruit in fruits:
    print("That fruit already exist in the list")
elif fruit not in fruits:
    fruits.append(fruit)
    appended_fruit = fruit  # Store the appended value
    print(f"{appended_fruit} has be added")
    print(fruits)
else:
    print("inavlid")

# Exercises: Level 3
# Here we have a person dictionary. Feel free to modify it!

person = {
    "first_name": "luffy",
    "last_name": "nika",
    "age": 22,
    "country": "Foosha",
    "is_marred": True,
    "skills": ["JavaScript", "React", "Node", "MongoDB", "Python"],
    "address": {"street": "Space street", "zipcode": "02210"},
}

#  Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if "skills" in person:
    skills = person["skills"]
    middle_idx = len(skills) // 2
    print(skills[middle_idx])

#  Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
if "skills" in person:
    skills = person["skills"]
    print("Python" in skills)

#  If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB,
# print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'),
# else print('unknown title') - for more accurate results more conditions can be nested!

skills = person["skills"]
skills_set = set(skills)

frontend = {"JavaScript", "React"}
backend = {"Node", "Python", "MongoDB"}
fullstack = {"React", "Node", "MongoDB"}

if fullstack.issubset(skills_set):
    print("He is a fullstack developer")
elif backend.issubset(skills_set):
    print("He is a backend developer")
elif frontend.issubset(skills_set):
    print("He is a front end developer")
else:
    print("unknown title")

#  If the person is married and if he lives in Foosha, print the information in the following format:
# luffy nika lives in Foosha. He is married.

if person["is_marred"] == True and person["country"] == "Foosha":
    print(f'{person["first_name"]} {person["last_name"]} lives in {person["country"]}. He is married')
