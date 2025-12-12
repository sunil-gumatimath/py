# While Loop

# Executes code as long as a condition evaluates to True. Always include a way to exit
# (e.g., increment a counter) to avoid infinite loops.

# syntax
# while condition:
#     code goes here

count = 0
while count < 5:
    print(count)
    count += 1  # Shorthand for count = count + 1

# prints 0, 1, 2, 3, 4

# In the above while loop, the condition becomes false when count is 5, which is when the loop stops.
# If we want to run a block of code once the condition is no longer true, we can use else.

# syntax
# while condition:
#     code goes here
# else:
#     code goes here

count = 0
while count < 5:
    print(count)
    count += 1
else:
    print(f"Loop ended, count is now {count}")

# The above loop condition will be false when count is 5, the loop stops, and execution continues
# with the else statement. As a result, "Loop ended, count is now 5" will be printed.


# Break and Continue - Part 1

# Break: We use break to exit or stop the loop immediately.

# syntax
# while condition:
#     code goes here
#     if another_condition:
#         break

count = 0
while count < 5:
    print(count)
    count += 1
    if count == 3:
        break

# The above while loop prints 0, 1, 2 then breaks when count becomes 3, so the loop stops early.


# Continue: Skips the rest of the current iteration and continues with the next one.

# syntax
# while condition:
#     code goes here
#     if another_condition:
#         continue

count = 0
while count < 5:
    if count == 3:
        count += 1  # Must increment before continue to avoid infinite loop
        continue
    print(count)
    count += 1

# The above loop prints 0, 1, 2, 4 (skips printing 3)
