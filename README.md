# Python Learning Repository

This repository is a guided learning path through core Python fundamentals. Each numbered directory is a module that introduces one concept at a time, and the `Assignment/` directory contains practice problems that reinforce those same concepts.

For a detailed, link-rich table of contents for every module, see **[index.md](./index.md)**.

## Who this is for

- Absolute beginners learning Python from scratch
- Learners who want a structured path instead of random examples
- Anyone revising the basics with short scripts plus exercises

## Before you start

- Install Python 3.x on your system
- Know how to run `python file_name.py` from a terminal or command prompt

## How to use this repository

For each step in the path:

1. Open the numbered module folder (for example, `01_variables/`).
2. Read the module `README.md` (where available) or skim the main code file.
3. Run the code file to see the examples and printed output.
4. Do the matching assignment file(s) in `Assignment/`.
5. Experiment: change values, add your own examples, and re-run.

Move through the steps in order. Each module builds on the previous ones.

## Step-by-step learning path

### Step 1 - Variables

- **Folder:** `01_variables/`
- **Practice:** `Assignment/variables_builtin_fun.py`
- **Focus:** Declaring variables, basic data types, simple lists and dictionaries, and using functions like `len()` on strings and names.

### Step 2 - Operations

- **Folder:** `02_operations/`
- **Practice:** `Assignment/operations.py`
- **Focus:** Arithmetic (`+`, `-`, `*`, `/`, `%`, `//`, `**`), comparison, logical, identity, and membership operators, with practical numeric problems.

### Step 3 - Strings

- **Folder:** `03_strings/`
- **Practice:** `Assignment/strings.py`
- **Focus:** Creating and combining strings, indexing and slicing, escape sequences, and common string methods for searching, formatting, and cleaning text.

### Step 4 - Lists

- **Folder:** `04_lists/`
- **Practice:** `Assignment/lists.py`
- **Focus:** Working with ordered collections: indexing, slicing, inserting, removing, copying, extending, counting, reversing, and sorting lists.

### Step 5 - Tuples

- **Folder:** `05_tuples/`
- **Practice:** `Assignment/tuples.py`
- **Focus:** Tuples as ordered, immutable collections, converting between tuples and lists, joining tuples, and checking membership.

### Step 6 - Sets

- **Folder:** `06_sets/`
- **Practice:** `Assignment/sets.py`
- **Focus:** Sets as collections of unique items, set operations (union, intersection, difference, symmetric difference), and subset/superset relationships.

### Step 7 - Dictionaries

- **Folder:** `07_dictionaries/`
- **Practice:** `Assignment/dictionaries.py`
- **Focus:** Key-value mappings, nested dictionaries, and dictionary methods such as `keys()`, `values()`, `items()`, `get()`, and `pop()`.

### Step 8 - Conditionals

- **Folder:** `08_conditionals/`
- **Practice:** `Assignment/conditionals.py`
- **Focus:** `if`, `if-else`, and `if-elif-else` blocks, short-hand (ternary) conditionals, nested conditions, and combining conditions with logical operators (`and`, `or`).

### Step 9 - Loops

- **Folder:** `09_Loops/`
- **Practice:** `Assignment/loops_01.py`, `Assignment/loops_02.py`
- **Focus:**
  - `while` loops with optional `else` blocks, including `break` and `continue`
  - `for` loops over lists, tuples, strings, dictionaries, and sets
  - Using `range()` to generate sequences of numbers
  - Nested loops, `for-else`, and `pass` as a placeholder

After completing Step 9, you will have covered the core control structures used in most Python programs.

## Assignments overview

The `Assignment/` directory contains a full set of exercises for every concept:

- Variables and built-in functions
- Operations and numerical problems
- Strings
- Lists
- Tuples
- Sets
- Dictionaries
- Conditionals and loops

Use these files to test your understanding after finishing each module.

## Environment setup (optional but recommended)

1. **Activate the virtual environment** (configured for Python 3.13):

   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

   On Command Prompt use: `.venv\Scripts\activate.bat`. Your prompt should show `(.venv)` when it is active.

2. **Install dependencies** (if any are listed):

   ```bash
   pip install -r requirements.txt
   ```

3. **Editor integration (VS Code)**

- Python interpreter is set to `./.venv/Scripts/python.exe`.
- Integrated terminal opens with the virtual environment activated.
