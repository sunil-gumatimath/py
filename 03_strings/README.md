# 03 - Python Strings

This module demonstrates how to work with strings in Python using the `strings.py` script. It is intended for beginners who want to understand string creation, manipulation, and the most common built-in methods by inspecting printed examples.

## Concepts Covered

- Single-line strings and their lengths
- Multi-line strings using both triple single and double quotes
- Concatenating strings with `+` and measuring the length of results
- Unpacking characters into variables
- Indexing from the start and end (negative indexing)
- Slicing substrings, including step slicing (`language[0:6:2]`)
- Escape sequences:
  - `\n` (newline)
  - `\t` (tab)
  - `\\` (backslash)
  - `\"` (double quote)
- String methods illustrated in the script:
  - `capitalize()`
  - `count()`
  - `endswith()`
  - `find()`
  - `format()`
  - `join()`
  - `strip()` with custom characters
  - `replace()`
  - `split()`
  - `title()`
  - `swapcase()`
  - `startswith()`

## Script Overview (`strings.py`)

The script demonstrates each concept with immediate print statements:

- Declares simple strings, prints them, and checks their lengths.
- Concatenates `first_name`, `space`, and `last_name` into `full_name` and investigates string length comparisons.
- Unpacks the word `Python`, then reuses it to showcase indexing, negative indexing, and diverse slicing patterns.
- Prints formatted sentences containing escape sequences.
- Walks through a catalog of string methods, displaying the return value of each call (e.g., `challenge.count('y')`, joining a list with `#, `).

Experiment by:

- Changing the base strings or introducing new ones to see how the methods react.
- Trying additional methods such as `upper()` or `lower()`.
- Updating slice ranges or step values to understand how slicing selects characters.
