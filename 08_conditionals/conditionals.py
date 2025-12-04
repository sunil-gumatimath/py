# By default, statements in Python script are executed sequentially from top to bottom. If the processing logic require so, the sequential flow of execution can be altered in two way:

# Conditional execution: a block of one or more statements will be executed if a certain expression is true
# Repetitive execution: a block of one or more statements will be repetitively executed as long as a certain expression is true. In this section, we will cover if, else, elif statements.
# The comparison and logical operators we learned in previous sections will be useful here.

# If Condition
# In python and other programming languages the key word if is used to check if a condition is true and to execute the block code. Remember the indentation after the colon.

# syntax
# if condition:
#    code

a = 3
if a > 0:
    print("A is a positive number ")

# If Else
# If condition is true the first block will be executed, if not the else condition will run.
# syntax
# if condition:
#     code
# else:
#     code

a = 3
if a < 0:
    print("A is a negative number")
else:
    print("A is a positive number")

# If Elif Else
# syntax
# if condition:
#     code
# elif condition:
#     code
# else:
#     code

a = 0
if a > 0:
    print("A is a positive number")
elif a < 0:
    print("A is a negative number")
else:
    print("A is zero")

# Short Hand
# syntax
# code if condition else code

a = 3
(
    print("A is positive") if a > 0 else print("A is negative")
)  # first condition met, 'A is positive' will be printed

# Nested Conditions
# Conditions can be nested
# syntax
# if condition:
#     code
#     if condition:
#     code

a = 0
if a > 0:
    if a % 2 == 0:
        print("A is a positive and even integer")
    else:
        print("A is a positive number")
elif a == 0:
    print("A is zero")
else:
    print("A is a negative number")

# If Condition and Logical Operators
# syntax
# if condition and condition:
#     code

a = 0
if a > 0 and a % 2 == 0:
    print("A is an even and positive integer")
elif a > 0 and a % 2 != 0:
    print("A is a positive integer")
elif a == 0:
    print("A is zero")
else:
    print("A is negative")

# If and Or Logical Operators
# syntax
# if condition or condition:
#     code

user = "James"
access_level = 3
if user == "admin" or access_level >= 4:
    print("Access granted!")
else:
    print("Access denied!")
