# 01 - Python Variables

This module introduces Python variables and core data types using the `variables.py` script. It is aimed at beginners who want to understand how to store, combine, and inspect data in Python by printing immediate feedback to the console.

## Concepts Covered

- Declaring and reading variables for personal information (names, location, age, marital status)
- Working with core data types:
  - `str` (first name, last name, country, city)
  - `int` (`age`)
  - `bool` (`is_married`)
  - `list` of skills
  - `dict` representing a person
- Basic operations:
  - Concatenating two strings into a full name
  - Measuring string length with `len()`
  - Slicing a list using full slicing syntax (`skills[::]`)
  - Printing dictionary contents

## Script Overview (`variables.py`)

The script walks through the following sequence:

- Declares `first_name`, `last_name`, `country`, `city`, `age`, and `is_married`.
- Creates a `skills` list and `person_info` dictionary.
- Prints each scalar value and shows its length where appropriate (first name, last name, full name).
- Demonstrates concatenating strings and slicing a list copy (`skills[::]`).
- Displays the entire dictionary to highlight key/value storage.

Experiment by:

- Changing the variable values to see the printed output change.
- Adding additional keys to `person_info` or extra items in `skills`.
- Introducing your own calculated fields (e.g., `birth_year`) and printing them.

## Practice Exercises

Practice your skills with the variable exercises in [Assignment/variables_builtin_fun.py](../Assignment/variables_builtin_fun.py):
- Declaring first name, last name, and full name variables
- Declaring country, city, age, and year variables
- Boolean variable declarations (is_married, is_true, is_light_on)
- Multiple variable declarations on one line
- Type checking using type() built-in function
- String length calculations using len() and comparisons
- Basic arithmetic operations (addition, subtraction, multiplication, division, modulus, exponentiation, floor division)
- Circle area and circumference calculations (with fixed radius and user input)
- User input for personal information (first name, last name, country, age)
- Python keywords exploration using help('keywords')

## Navigation

[← Back to Main README](../README.md) | [Next: Operations →](../02_operations/README.md)

## Related Modules

- **Next**: [02 - Operations](../02_operations/README.md) - Learn how to manipulate and compare data
- **See also**: [Table of Contents](../index.md) for all modules
