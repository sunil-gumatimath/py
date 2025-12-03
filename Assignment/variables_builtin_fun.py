# Day 2: 30 Days of python programming

# Level 1: Variable Declarations

# Declare first name
first_name = "Ted"

# Declare last name
last_name = "Nika"

# Declare full name
full_name = first_name + " " + last_name

# Declare country
country = "India"

# Declare city
city = "Bangalore"

# Declare age
age = 24

# Declare year
year = 2023

# Declare is_married
is_married = False

# Declare is_true
is_true = True

# Declare is_light_on
is_light_on = True

# Declare multiple variables on one line
x, y, z = 10, 20, 30

# Level 2: Built-in Functions and Operations

# Check data types of all variables
print("Data types:")
variables = [
    first_name,
    last_name,
    full_name,
    country,
    city,
    age,
    year,
    is_married,
    is_true,
    is_light_on,
    x,
    y,
    z,
]
variable_names = [
    "first_name",
    "last_name",
    "full_name",
    "country",
    "city",
    "age",
    "year",
    "is_married",
    "is_true",
    "is_light_on",
    "x",
    "y",
    "z",
]
for name, var in zip(variable_names, variables):
    print(f"{name}: {type(var)}")

# Find length of first name
first_name_length = len(first_name)
print(f"Length of first name: {first_name_length}")

# Compare lengths of first and last name
last_name_length = len(last_name)
print(f"Length of last name: {last_name_length}")
if first_name_length > last_name_length:
    print("First name is longer than last name")
elif first_name_length < last_name_length:
    print("Last name is longer than first name")
else:
    print("First name and last name have the same length")

# Arithmetic operations
num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one**num_two
floor_division = num_one // num_two

print(f"total: {total}")
print(f"diff: {diff}")
print(f"product: {product}")
print(f"division: {division}")
print(f"remainder: {remainder}")
print(f"exp: {exp}")
print(f"floor_division: {floor_division}")

# Circle calculations
radius = 30
pi = 3.14159
area_of_circle = pi * radius**2
circum_of_circle = 2 * pi * radius

print(f"Area of circle: {area_of_circle}")
print(f"Circumference of circle: {circum_of_circle}")

# Take radius as user input and calculate area
radius_input = float(input("Enter radius: "))
area_input = pi * radius_input**2
print(f"Area with input radius: {area_input}")

# Get user input for personal details
first_name_input = input("Enter first name: ")
last_name_input = input("Enter last name: ")
country_input = input("Enter country: ")
age_input = int(input("Enter age: "))

print(f"First name: {first_name_input}")
print(f"Last name: {last_name_input}")
print(f"Country: {country_input}")
print(f"Age: {age_input}")

# Display Python keywords
print("Python reserved words or keywords:")
help("keywords")
