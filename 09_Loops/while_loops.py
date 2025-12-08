# While Loop

# Executes code as long as a condition evaluates to True. Use with a way to exit
# (e.g., increment a counter) to avoid infinite loops.

# syntex
# while condition:
# code goes here

count = 0
while count < 5:
    print(count)
    count = count + 1

#  prints 0 to 4

# In the above while loop, the condition becomes false when count is 5. That is when the loop stops. If we are interested to run block of code once
# the condition is no longer true, we can use else.

# syntex
# while condition:
# code goes here
# else:
# code goes here

count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print(count)

# The above loop condition will be false when count is 5 and the loop stops, and execution starts the else statement. As a result 5 will be printed.


# Break and Continue - Part 1
# Break: We use break when we like to get out of or stop the loop.

# syntax
# while condition:
#     code goes here
#     if another_condition:
#         break

count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break
# The above while loop only prints 0, 1, 2, but when it reaches 3 it stops.

# Continue: With the continue statement we can skip the current iteration, and continue with the next:
# syntax
# while condition:
#     code goes here
#     if another_condition:
#         continue
count = 0
while count < 5:
    if count == 3:
        count = count + 1
        continue
    print(count)
    count = count + 1
