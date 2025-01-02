# Advent of Code 2024 Solutions

This repository contains my solutions to the Advent of Code 2024 challenges. Each day's task is divided into two parts, and I have solved each part in separate Python files. The solutions are organized by day and stage.

## Folder Structure

- `inputs/`: This folder contains the input files for each task. The input files are named `input.txt`, `input2.txt`, etc., corresponding to the task number.
- `1_1.py`, `1_2.py`, `2_1.py`, `2_2.py`, etc.: These are the Python scripts containing my solutions for each task. The file names follow the format `<day>_<stage>.py` where:
  - `<day>` represents the task number (e.g., `1`, `2`, `3`, etc.).
  - `<stage>` represents the stage of the task (`1` for the first part, `2` for the second part).

## Task Overview

Below is a brief overview of the tasks I have solved so far, along with the corresponding Python files for each stage:

### Day 1:

- **Task Description (1_1.py)**: Given two lists of location IDs, pair the numbers by sorting both lists and calculating the sum of absolute differences between corresponding elements in each list. The goal is to find the total distance by summing up these differences.
- **Task Description (1_2.py)**: Given two lists of location IDs, calculate the similarity score by iterating through each number in the left list. For each number, count how many times it appears in the right list, then multiply the number by its count and sum all these products to get the total similarity score.

### Day 2:

- **Task Description (2_1.py)**: Given a list of reports, each containing levels of numbers, the goal is to determine how many reports are safe. A report is safe if the numbers are either all increasing or all decreasing, and the difference between any two adjacent levels is between 1 and 3 (inclusive). A report is considered safe if it satisfies both conditions.
- **Task Description (2_2.py)**: Given a list of reports, each containing levels of numbers, the goal is to determine how many reports are safe. A report is safe if the numbers are either all increasing or all decreasing, the difference between any two adjacent levels is between 1 and 3 (inclusive) and in the case of an unsafe report, if removing one level would make it safe. A report is considered safe if it satisfies all conditions.

### Day 3:

- **Task Description (3_1.py)**: Search a given list of characters for valid multiplication instructions (mul(X,Y)) and ignore any invalid characters or malformed instructions. Multiply the numbers in valid instructions and sum the results.
- **Task Description (3_2.py)**: Search a given list of characters for valid multiplication (mul(X,Y)) and conditional (do(), don't()) instructions and ignore any invalid characters or malformed instructions. Multiply the numbers in enabled valid instructions and sum the results.

### Day 4:

- **Task Description (4_1.py)**: Scan a given word search grid to count all occurrences of the word "XMAS". The word can appear horizontally, vertically, diagonally, backwards and also overlap other words.
-  **Task Description (4_2.py)**: Scan a given word search grid to count all occurrences of "XMAS" in the shape of an "X", where "MAS" can be written forwards or backwards. Count the total number of times this "X-MAS" pattern appears in the grid. "MAS" should appear in a pattern like:
```
M.S
.A.
M.S
```

## How to Run the Solutions

To run the solutions for a particular task, you can follow these steps:

1. Clone the repository to your local machine.
2. Navigate to the folder where the Python script is located.
3. Run the Python script using the command:
   python <script_name>.py

Make sure you have python 3.x installed on your system. The solutions do not require any external dependencies.