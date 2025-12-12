# Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(num1, num2):
    sum = num1 + num2
    return sum


print(add_two_numbers(10, 20))

# Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.


def area_of_circle(r):
    PI = 3.142
    area = PI * r * r
    return area


print(area_of_circle(10))

# Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments.
# Check if all the list items are number types. If not do give a reasonable feedback.

def add_all_nums(*arg):
    total = 0
    for item in arg:
        if not isinstance(item,(int,float)):
            return "All arguments must be numbers"
        total = total + item
    return total
    
print(add_all_nums(1, 2, 3, 4))        # 10
print(add_all_nums(1, "two", 3))  