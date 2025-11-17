# Python Learning Repository

This repository is a collection of small Python scripts organized by topic. Each module focuses on a fundamental Python concept and mirrors the examples found in the accompanying source file.

**For a more detailed table of contents with navigation links, see [index.md](./index.md).**

## Prerequisites

- Python 3.x installed on your system
- Basic familiarity with running commands in a terminal/command prompt

## Project Structure

- `01-variables/`
  - Declares core pieces of personal data: names, location, age, marital status.
  - Introduces list and dictionary literals (`skills`, `person_info`) and prints them directly.
  - Uses `len()` to inspect individual strings and a concatenated full name.
- `02-operations/`
  - Runs through the arithmetic operators (`+`, `-`, `*`, `/`, `%`, `//`, `**`) using both literal expressions and stored variables.
  - Demonstrates float and complex literals, as well as reusing variables across multiple calculations.
  - Includes practical problems: areas of a circle and rectangle, and a simple weight computation (`mass * gravity`).
  - Shows comparison, logical, identity, and membership operators with printed outcomes for every expression.
- `03-strings/`
  - Builds single-line and multi-line strings, prints their lengths, and combines first and last names.
  - Unpacks characters, explores indexing (positive and negative), and slices strings with different step values.
  - Highlights escape sequences for newlines, tabs, backslashes, and quotes.
  - Calls a suite of built-in string methods: `capitalize`, `count`, `endswith`, `find`, `format`, `join`, `strip`, `replace`, `split`, `title`, `swapcase`, and `startswith`.
- `04-lists/`
  - Starts with a typed empty list before showcasing several themed lists (fruits, vegetables, animal products, web tech, countries).
  - Prints list contents, lengths, and demonstrates positive/negative indexing plus multiple slice patterns.
  - Updates items by index, checks membership, appends and inserts new elements.
  - Removes data with `remove`, `pop`, and `del` (including an intentional `NameError` when the deleted list is accessed).
  - Covers `clear`, `copy`, list concatenation and `extend`, followed by counting, indexing, reversing, and sorting examples.
- `05-tuples/`
  - Introduces tuples as ordered, immutable collections.
  - Demonstrates creating tuples, accessing elements by index, slicing, converting to lists for modification.
  - Covers membership checks, joining tuples, and deleting tuples entirely.
- `06-sets/`
  - Explores sets as unordered collections of unique elements.
  - Demonstrates set creation, adding and removing items.
  - Covers set operations: union, intersection, difference, symmetric difference.
  - Shows subset, superset, and disjoint set relationships.
  - Highlights set methods like `add`, `update`, `remove`, `pop`, `clear`, and comparison operations.

Each directory contains a dedicated `README.md` describing its script in more detail.

- `Assignment/`
  - Contains comprehensive practice exercises for each module to reinforce learning concepts
  - Includes assignments for variables, operations, strings, lists, tuples, and sets
  - **variables_builtin_fun.py**: Variable declarations, type checking, arithmetic operations, circle calculations, user input
  - **operations.py**: 23 exercises covering geometry calculations, slope/distance, quadratic equations, type conversions, pay calculator
  - **strings.py**: String manipulation exercises including concatenation, case conversion, searching, slicing, formatting
  - **lists.py**: Extensive list exercises with IT companies, student ages, countries, and multi-level list operations
  - **tuples.py**: Tuple creation, joining, converting, slicing, and membership exercises
  - **sets.py**: Set operations with IT companies, age sets, union/intersection/difference operations, unique word finding

Each module directory contains a dedicated `README.md` describing its script in more detail.

## Recommended Usage

- Read the module's `README.md` to understand what each script demonstrates.
- Run the script to see outputs.
- Practice with the corresponding assignment file in the `Assignment/` directory.
- Modify values, add new examples, and re-run to reinforce understanding.
- Complete the exercises in the assignment files to apply what you've learned.

## Learning Path

Follow this recommended order for beginners:

1. **Variables** → Start here to understand basic data storage
2. **Operations** → Learn how to manipulate and compare data
3. **Strings** → Master text processing
4. **Lists** → Work with ordered collections
5. **Tuples** → Understand immutable sequences
6. **Sets** → Explore unique collections and set theory

## Audience

- Beginners learning Python fundamentals
- Anyone looking for quick, focused examples of core Python concepts
