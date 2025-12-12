# Function with Default Parameters
# Sometimes we pass default values to parameters, when we invoke the function. If we do not pass arguments when calling the function, their default values will be used.
# syntax
# Declaring a function
# def function_name(param = value):
#     codes
#     codes
# # Calling function
# function_name()
# function_name(arg)


def greeting(name="joyboy"):
    message = name + " welcome"
    return message


print(greeting("Nika"))
print(greeting())


def generate_full_name(first_name="nika", last_name="joyboy"):
    space = " "
    full_name = first_name + space + last_name
    return full_name


print(generate_full_name("luffy", "monkey"))
print(generate_full_name())


def calculate_age(birth_year, current_year=2025):
    age = current_year - birth_year
    return age


print("Age: ", calculate_age(2000, 2024))
print("Age: ", calculate_age(2000))


def weight_of_object(mass, gravity=9.91):
    weight = str(mass * gravity) + "N"
    return weight


print(
    "Weight of an object in Newtons: ", weight_of_object(100)
)  # 9.81 - average gravity on Earth's surface
print(
    "Weight of an object in Newtons: ", weight_of_object(100, 1.62)
)  # gravity on the surface of the Moon

# Arbitrary Number of Arguments
# If we do not know the number of arguments we pass to our function, we can create a function which can take arbitrary number of arguments by adding * before the parameter name.

# syntax
# Declaring a function
# def function_name(*args):
#     codes
#     codes
# # Calling function
# function_name(param1, param2, param3,..)


def sum_of_all(*nums):
    total = 0
    for num in nums:
        total += num
    return total


print(sum_of_all(10, 20, 30))


# Default and Arbitrary Number of Parameters in Functions
def generate_groups(team, *args):
    print(team)
    for i in args:
        print(i)


print(generate_groups("Team-straw-hat", "luffy", "zoro", "sanji", "franki"))


# Function as a Parameter of Another Function
# You can pass functions around as parameters
def square_number(n):
    return n * n


def do_something(f, x):
    return f(x)


print(do_something(square_number, 3))
