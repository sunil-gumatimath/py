# Functions

# A function in Python is a reusable block of code that performs a specific task. It promotes modularity and reduces repetition.

# Declaring and Calling a Function

# When we make a function, we call it declaring a function. When we start using the it, we call it calling or invoking a function.
# Function can be declared with or without parameters.

# Syntax
# def function_name():
#     codes
#     codes

# function_name()

# Function without Parameters
# Function can be declared without parameters.


def generate_full_name():
    first_name = "luffy"
    last_name = "nika"
    space = " "
    full_name = first_name + space + last_name
    print(full_name)


generate_full_name()


def add_two_numbers():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    print(total)


add_two_numbers()

# Function Returning a Value - Part 1
# Function can also return values, if a function does not have a return statement, the value of the function is None.
# Let us rewrite the above functions using return. From now on, we get a value from a function when we call the function and print it.


def generate_full_name():
    first_name = "luffy"
    last_name = "nika"
    space = " "
    full_name = first_name + space + last_name
    return full_name


print(generate_full_name())


def add_two_numbers():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    return total


print(add_two_numbers())

# Function with Parameters
# In a function we can pass different data types(number, string, boolean, list, tuple, dictionary or set) as a parameter

# Single Parameter: If our function takes a parameter we should call our function with an argument

# syntax
# Declaring a function
#   def function_name(parameter):
#     codes
#     codes
#   # Calling function
#   print(function_name(argument))


def greetings(name):
    message = name + " hello there how you doing"
    return message


print(greetings("sunil"))


def add_ten(num):
    return num + 10


print(add_ten(100))


def square_number(x):
    return x * x


print(square_number(10))


def area_of_circle(r):
    PI = 3.14
    area = PI * r**2
    return area


print(area_of_circle(10))


def sum_of_numbers(n):
    total = 0
    for i in range(n + 1):
        total += i
    return total


print(sum_of_numbers(10))
print(sum_of_numbers(100))

# Two Parameters: A function may or may not have a parameter or parameters. A function may also have two or more parameters.
# If our function takes parameters we should call it with arguments

# Syntax
# Declaring a function
#   def function_name(para1, para2):
#     codes
#     codes
# Calling function
#   print(function_name(arg1, arg2))


def generate_full_name(first_name: str, last_name: str):
    space = " "
    return first_name + space + last_name


print("Full Name: ", generate_full_name("luffy", "nika"))


def sum_two_number(num1: int, num2: int):
    sum = num1 + num2
    return sum


print("Sum of two numbers: ", sum_two_number(10, 20))


def calculate_age(current_year, birth_year):
    age = current_year - birth_year
    return age


print("Age :", calculate_age(2025, 2000))


def is_even(n):
    if n % 2 == 0:
        print("even")
        return True
    return False


print(is_even(10))
print(is_even(5))


def find_even_numbers(n):
    evens = []
    for i in range(n + 1):
        if i % 2 == 0:
            evens.append(i)
    return evens


print(find_even_numbers(66))
