# 04 - Python Lists

This module demonstrates how to work with lists in Python using the `lists.py` script. It is intended for beginners who want to understand list creation, indexing, slicing, modification, and common list methods.

## Concepts Covered

- Creating lists:
  - Non-empty lists (e.g. fruits, vegetables, animal products, technologies, countries)
  - Typed empty list: `empty_list: list[int] = []`
- Inspecting lists:
  - Printing lists
  - Getting length with `len()`
- Indexing:
  - Accessing items by positive index
  - Accessing items by negative index
  - Finding the last index using `len(list) - 1`
- Slicing:
  - Basic slicing with start/stop
  - Slicing with negative indices
  - Getting all or partial segments of a list
- Modifying lists:
  - Updating elements by index (positive and negative)
- Membership:
  - Checking if an element exists using `in`
- Adding items:
  - `append()` to add at the end
  - `insert()` to add at a specific position
- Removing items:
  - `remove()` to delete by value
  - `pop()` to delete last element or by index
  - `del` to delete by index or the entire list
- Clearing and copying:
  - `clear()` to empty a list
  - `copy()` and slicing (`[:]`) to clone lists
- Combining lists:
  - Using `+` to concatenate lists
  - Using `extend()` to add all elements from another list
- Counting, indexing, ordering:
  - `count()` to count occurrences
  - `index()` to find the position of an element
  - `reverse()` to reverse order
  - `sort()` to sort ascending/descending

## Script Overview (`lists.py`)

The script walks through:

- Realistic examples with fruits, vegetables, and numbers
- Step-by-step prints showing the effect of each operation
- Examples of joining multiple lists into a single sequence
- Demonstrations of counting, indexing, reversing, and sorting

This provides a practical overview of how lists behave and how they are commonly manipulated in Python.

## How to Run

From the repository root:

```bash
cd 04-lists
python lists.py
```

Experiment by:

- Adding new items and re-running the script
- Changing indices and slice ranges
- Trying other list methods like `min()`, `max()`, or list comprehensions in your own extensions
