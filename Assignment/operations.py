# 1. Declare your age as an integer variable
age: int = 25

# 2. Declare your height as a float variable
height: float = 6.1

# 3. Declare a variable that stores a complex number
num_complex = 1 + 5j

# 4. Triangle area (prompt)
base: float = float(input("Enter base: "))
tri_height: float = float(input("Enter height: "))
triangle_area = 0.5 * base * tri_height
print(f"The area of the triangle is {triangle_area}")

# 5. Triangle perimeter (prompt)
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
perimeter = a + b + c
print(f"The perimeter of the triangle is {perimeter}")

# 6. Rectangle area & perimeter (prompt)
length: float = float(input("Enter the length: "))
width: float = float(input("Enter the width: "))
rect_area = length * width
rect_perimeter = 2 * (length + width)
print(f"Area of rectangle: {rect_area}")
print(f"Perimeter of rectangle: {rect_perimeter}")

# 7. Circle area & circumference (prompt) using pi = 3.14
pi = 3.14
rad: float = float(input("Enter the radius: "))
circle_area = pi * rad * rad
circumference = 2 * pi * rad
print(f"Area of circle: {circle_area}")
print(f"Circumference of circle: {circumference}")

# 8. Line y = 2x - 2: slope and intercepts
slope = 2.0
y_intercept = -2.0
x_intercept = -y_intercept / slope
print(f"Slope: {slope}")
print(f"Y-intercept: {y_intercept}")
print(f"X-intercept: {x_intercept}")

# 9. Slope and Euclidean distance between (2,2) and (6,10)
x1, y1 = 2, 2
x2, y2 = 6, 10
slope_2 = (y2 - y1) / (x2 - x1)
import math

distance = math.hypot(x2 - x1, y2 - y1)
print(f"Slope between (2,2) and (6,10): {slope_2}")
print(f"Distance between points: {distance}")

# 10. Compare slopes (task 8 and 9)
if slope == slope_2:
    print("Both slopes are equal.")
else:
    print("The slopes are different.")


# 11. Quadratic y = x^2 + 6x + 9, test values and find root(s)
def quad_y(x):
    return x**2 + 6 * x + 9


for x in [-5, -3, -1, 0, 1]:
    print(f"x={x}, y={quad_y(x)}")

# 12. Length of 'python' and 'dragon' and falsy comparison
var1 = "python"
var2 = "dragon"
print(f"Length of python: {len(var1)}")
print(f"Length of dragon: {len(var2)}")
print("Are lengths equal?", len(var1) == len(var2))  # False

# 13. Use `and` operator to check if 'on' is found in both
print("'on' in python?", "on" in var1)
print("'on' in dragon?", "on" in var2)
print("'on' in both?", ("on" in var1) and ("on" in var2))  # True

# 14. Check if 'jargon' is in sentence
sentence = "I hope this course is not full of jargon"
print("'jargon' in sentence?", "jargon" in sentence)  # True

# 15. The sentence "There is no 'on' in both dragon and python" is false.
print(
    "'on' present in python and dragon? ->", ("on" in var1) and ("on" in var2)
)  # True

# 16. Convert length of 'python' to float then to string
py = "python"
len_py = len(py)  # int 6
len_float = float(len_py)  # float 6.0
len_str = str(len_float)  # string '6.0'
print(f"type: {type(len_str)} value: {len_str}")

# 17. Check evenness of a number
num = 10  # example
is_even = num % 2 == 0
print(f"Is {num} even? {is_even}")

# 18. Check if 7//3 == int(2.7)
result = (7 // 3) == int(2.7)
print("7//3 == int(2.7)?", result)  # True

# 19. Check if type('10') == type(10)
print("type('10') == type(10)?", type("10") == type(10))  # False

# 20. Check if int('9.8') is equal to 10
try:
    v = int("9.8")  # will raise ValueError
except ValueError:
    v = int(float("9.8"))  # -> 9
print("int(float('9.8')) == 10 ?", v == 10)  # False

# 21. Weekly earning from hours and rate per hour
hours = float(input("Enter hours: "))
rate_per_hour = float(input("Enter rate per hour: "))
weekly_earning = hours * rate_per_hour
print(f"Your weekly earning: {weekly_earning}")

# 22. Seconds lived (given number of years)
no_of_years = int(input("Enter number of years you have lived: "))
seconds_lived = no_of_years * 365 * 24 * 3600
print(f"You have lived approximately {seconds_lived} seconds.")

# 23. Print the requested table
for i in range(1, 6):
    print(i, 1, i, i**2, i**3)
