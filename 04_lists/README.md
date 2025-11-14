# 04 - Python Lists

This module demonstrates how to work with lists in Python using the `lists.py` script. It is intended for beginners who want to understand list creation, indexing, slicing, modification, and common list methods through short, targeted print statements.

## Concepts Covered

- Creating lists:
  - Typed empty list annotation: `empty_list: list[int] = []`
  - Populated lists (fruits, vegetables, animal products, web technologies, countries)
- Inspecting lists:
  - Printing contents
  - Measuring length with `len()`
- Indexing and slicing:
  - Positive and negative indexing
  - Finding the last index via `len(list) - 1`
  - Standard slices, negative slices, and full-list slices
- Modifying lists:
  - Replacing items by index (including negative indices)
  - Membership checks with the `in` operator
- Adding items:
  - `append()` for end insertion
  - `insert()` for targeted positions
- Removing items:
  - `remove()` for value-based deletion
  - `pop()` with and without an index
  - `del` for removing items and deleting the entire list (illustrated by an intentional `NameError` after `del fruits`)
- Clearing and copying:
  - `clear()`, `copy()`, and slicing (`[:]`)
- Combining lists:
  - Concatenation with `+`
  - Extending lists with `extend()`
- Counting, indexing, and ordering:
  - `count()` and `index()`
  - `reverse()` and `sort()` (ascending and descending)

## Script Overview (`lists.py`)

The script is broken into clearly labelled sections:

- Starts by measuring the length of an empty list, then prints several themed list variables.
- Demonstrates indexing, negative indexing, and different slice ranges on the `fruits` list.
- Shows how reassignment works for first, middle, and last elements.
- Performs membership checks before moving on to `append()` and `insert()` examples.
- Covers the three main deletion patterns (`remove`, `pop`, `del`) and highlights the runtime error raised when trying to print a deleted variable.
- Resets the lists to demonstrate `clear()`, `copy()`, concatenation, `extend()`, counting, indexing, reversing, and sorting.

Experiment by:

- Substituting your own list items (e.g., hobbies, cities, numbers).
- Commenting out the `del fruits` block if you want the script to run to completion without an error.
- Adding practice with other list helpers such as `min()`, `max()`, or list comprehensions.

## Navigation

[← Previous: Strings](../03_strings/README.md) | [Back to Main README](../README.md) | [Next: Tuples →](../05_tuples/README.md)

## Related Modules

- **Previous**: [03 - Strings](../03_strings/README.md) - Master text processing
- **Next**: [05 - Tuples](../05_tuples/README.md) - Understand immutable sequences
- **See also**: [Table of Contents](../index.md) for all modules
