import math


# Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(num1, num2):
    total = num1 + num2
    return total


# Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def area_of_circle(r):
    PI = 3.142
    return PI * r * r


# Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(*arg):
    total = 0
    for item in arg:
        if not isinstance(item, (int, float)):
            return "All arguments must be numbers"
        total = total + item
    return total


print(add_all_nums(1, 2, 3, 4))  # 10
print(add_all_nums(1, "two", 3))


# Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to_fahrenheit.
def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


# Write a function called check_season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def check_season(month):
    month = month.lower()

    if month in ["december", "january", "february"]:
        return "Winter"
    elif month in ["march", "april", "may"]:
        return "Spring"
    elif month in ["june", "july", "august"]:
        return "Summer"
    elif month in ["september", "october", "november"]:
        return "Autumn"
    else:
        return "Invalid month"


# Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope(x1, y1, x2, y2):
    if x2 - x1 == 0:
        return "Slope is undefined"
    return (y2 - y1) / (x2 - x1)


# Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
def solve_quadratic_eqn(a, b, c):
    discriminant = b**2 - 4 * a * c

    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return x1, x2
    elif discriminant == 0:
        x = -b / (2 * a)
        return x
    else:
        return "No real solutions"


# Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(items):
    for item in items:
        print(item)


# Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
def reverse_list(arr):
    reversed_items = []
    for item in arr:
        reversed_items.insert(0, item)
    return reversed_items


print(reverse_list([1, 2, 3, 4, 5]))
print(reverse_list(["A", "B", "C"]))


# Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items(items):
    capitalized_items = []
    for item in items:
        capitalized_items.append(item.capitalize())
    return capitalized_items


print(capitalize_list_items(["apple", "banana", "mango"]))


# Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
def add_item(items, item):
    items.append(item)
    return items


food_staff = ["Potato", "Tomato", "Mango", "Milk"]
print(add_item(food_staff, "Meat"))


# Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
def remove_item(items, item):
    if item in items:
        items.remove(item)
    return item


food_staff = ["Potato", "Tomato", "Mango", "Milk"]
print(remove_item(food_staff, "Mango"))  # ['Potato', 'Tomato', 'Milk'];
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))  # [2, 7, 9]


# Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
def sum_of_numbers(n):
    total = 0
    for i in range(1, n + 1):
        total = total + i
    return total


print(sum_of_numbers(5))  # 15
print(sum_of_numbers(10))  # 55
print(sum_of_numbers(100))  # 5050


# Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
def sum_of_odds(n):
    total = 0
    for i in range(1, n + 1):
        if i % 2 != 0:
            total += i
    return total


# Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
def sum_of_even(n):
    total = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            total += i
    return total
