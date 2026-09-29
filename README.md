# Password "Checkah" PythonStyle

A Python learning project that demonstrates how a brute-force password search works by generating possible character combinations and comparing them against a password stored by my python password "holdah".

This project was built to practice Python fundamentals, program structure, performance measurement, and debugging.

## Features

- Generates password combinations using `itertools.product()`
- Searches across multiple password lengths
- Supports:
  - Lowercase letters
  - Uppercase letters
  - Numbers
  - Punctuation
- Counts the total number of guesses
- Measures execution time with `time.perf_counter()`
- Calculates guesses per second
- Uses a separate password program to create and change the local password
- Uses reusable functions imported between Python files

## What I Learned

This project helped me practice:

- Nested loops
- `break`
- Functions and return values
- Importing functions from another Python module
- `if __name__ == "__main__"`
- `itertools.product()`
- The `string` module
- File handling with `pathlib.Path`
- Measuring program performance
- Counting iterations
- f-string formatting
- Debugging Python programs
- Understanding how quickly brute-force search spaces grow

## Example Output

```text
=============================
+++++++++++++++++++++++++++++
        Password Checkah
+++++++++++++++++++++++++++++
=============================

*****
54246
*****
Password Found

Time: 437.98
Guesses: 457,617,865
Guesses per second: 1,044,839.20