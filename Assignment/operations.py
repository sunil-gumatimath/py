# Declare your age as integer variableage : int = 25
# Declare your height as a float variable

height : float = 6.1

# Declare a variable that store a complex number
num = 1 + 5j

# Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
base : float = float(input('Enter the base : '))
height : float = float(input('Enter the height : '))
area : float = 0.5 * base * height
print(f'Area of triangle : {area}')

# Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
a = float(input('Enter side a : '))
b = float(input('Enter side b : '))
c = float(input('Enter side c : '))
perimeter = a + b + c
print(f'perimeter of the triangle {perimeter}')

# Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length : float = input('Enter the length : ')
width : float = input('Enter the width : ')
rect_area = length * width
rect_perimeter = 2 * (length + width)
print(f'area of rectangle : {rect_area}')
print(f'perimeter of rectangle : {rect_perimeter}')

# Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
pi : float = 3.14
rad : float = input('enter the radius : ')
area : float = pi * rad * rad
print(f'area of circle : {area}')
circumference : float = 2 * pi * rad
print(f'circumference of circle : {circumference}')

# Calculate slope, x-intercept and y-intercept of y = 2x - 2
slope: float = 2
y_intercept: float = -2

# x-intercept formula: -c / m
x_intercept: float = -y_intercept / slope

print(f"Slope: {slope}")
print(f"Y-intercept: {y_intercept}")
print(f"X-intercept: {x_intercept}")

# Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
# Compare the slopes in tasks 8 and 9.
# Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.

# Find the length of 'python' and 'dragon' and make a falsy comparison statement.
var1 : str = 'python'
var2 : str = 'dragon'
print(f'length of python {len(var1)}')
print(f'length of dragon {len(var2)}')
print(len(var1) == len(var2))

# Use and operator to check if 'on' is found in both 'python' and 'dragon'
print('on' in 'python')
print('on' in 'dragon')

# I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
sentence : str = 'I hope this course is not full of jargon'
print('jargon' in sentence)

# There is no 'on' in both dragon and python
print('on' in 'python')
print('on' in 'dragon')

# Find the length of the text python and convert the value to float and convert it to string
py : str = 'python'
# int
len_py : int = len(py)
# float
len_float : float = float(len_py)
# String
len_str : str = str(len_float)
print(f'type : {type(len_str)} value {len_str}')

# Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
num = 10   # example number
even: bool = (num % 2 == 0)
print(even)

# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
result = (7//3) == int(2.7)
print(result)

# Check if type of '10' is equal to type of 10
print(type('10') == type(10))

# Check if int('9.8') is equal to 10
result = int(9.8) == int(10)
print(result)

# Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours : int = int(input('Enter hours : '))
rate_per_hour : int = int(input('Enter rate per hour : '))
weekly_earning : int = hours * rate_per_hour
print(f'your weekly earning : {weekly_earning}')

# Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
no_of_years : int = int(input('Enter number of years you have lived : '))
seconds_lived = no_of_years * 365 * 24 * 3600
print(f'You have lived approximately {seconds_lived} seconds.')

# Write a Python script that displays the following table
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125
for i in range(1,6):
    print(i,1,i,i**2,i**3)
