# Student Information
* **Name:** Ceren Karademir
* **Student Number:** 2404109062
* **Department:** Management Information Systems
* **Course Name:** MIS203 Basic Programming

---

### AI Tool Usage
* **AI Tool Used:** Gemini
* **Prompt Used:** Write a simple Python program that asks the user for Name, Department, Age, and Career Goal, then prints a short student profile.
* **What did you change?:** I updated the prompt text to English and added formatted print output to match the required example structure.



## Week 02

* **AI Tool Used:** Gemini
* **Prompt Used:** Write a Python program named grade_calculator.py using an infinite while loop that calculates student letter grades and average scores.
* **What did you change?** I adjusted the input prompt messages and score validation logic to strictly match the assignment instructions and formatting requirements.
* **What does break do in your program?** When the user enters the letter 'q', it exits the while loop; this stops data entry and displays the previous statistics on the screen.




* # Lab Quiz 01 - Student Introduction Card

## Testing Summary
- **Test Executed:** I ran the program in the terminal and tested it using my own details (Name, Student ID, Department, GitHub Username, and Programming Goal).
- **Change Made After Testing:** After testing the initial output, I increased the length of the border lines (`=`) from 30 to 40 characters to ensure longer input texts fit nicely without awkward line breaks.
- **Boundary/Error Case (Stretch Task):** I tested a boundary case by providing an empty input for the name field and pressing Enter. The program executed without crashing, but it displayed a blank space next to the `Name:` label.
- **Future Improvement:** In the future, input validation (such as a `while` loop or checking if `.strip()` is empty) can be added to prompt the user again if required fields are left blank.


## Concept Explanations
1. **`input()` function:** Reads user input from the terminal/console as a string and stores it in a variable for later use.
2. **`print()` function:** Outputs formatted text, variables, or `f-strings` to the terminal/console screen for the user to see.


# Week 2 Lab Quiz: Two-Item Purchase Quote

## Testing Summary
- **Test Executed:** Tested the program using the required test case (2 x 50 TRY and 1 x 80 TRY, delivery fee: 20 TRY, tax: 10%).
  - Line 1: 2 x 50.00 = 100.00 TRY
  - Line 2: 1 x 80.00 = 80.00 TRY
  - Subtotal: 180.00 TRY
  - Tax (10%): 18.00 TRY
  - Delivery Fee: 20.00 TRY
  - **Final Total:** 218.00 TRY (Verified against expected value).
- **Change Made After Testing:** Applied `:.2f` formatting to all monetary outputs to guarantee two decimal places for all amounts.
- **Error/Boundary Testing (Stretch Task):** Tried typing alphabetical characters (e.g., `"two"`) for the quantity input. The program raised a `ValueError` and stopped execution.
- **Future Improvement:** Incorporate input validation loops or `try-except` blocks to handle invalid non-numeric entries gracefully.

## Concept Explanation
- **Why `input()` must be converted:** The `input()` function in Python always stores user input as a string data type (`str`). Mathematical operators cannot perform numeric arithmetic on strings directly. Converting inputs using `int()` for quantities and `float()` for prices and fees casts these inputs into numerical data types, enabling arithmetic operations.


## Week 03

- **AI Tool Used:** Gemini
- **Prompt Used:** "Create a Python program named ticket_office.py that calculates cinema ticket prices based on age, day, and student status..."
- **What did you change?:** I adjusted the order of condition checks and formatted the floating-point numbers for exact output matching.
- **Tests:**
  1. Input: Age 5 (Weekend) -> Result: 0.00 TRY (Free)
  2. Input: Age 20, Student Yes (Weekday) -> Result: 140.00 TRY (Student)
  3. Input: Age 65 (Weekday) -> Result: 100.00 TRY (Senior)
- **Why does the order of the rules matter?:**
  If the student rule came before the child rule, a 10-year-old student would receive only a 30% student discount instead of the 40% child discount they are eligible for. The order ensures customers get the highest prioritized discount intended for their group.


# Dorm Laundry System

A simple Python script simulating a dorm laundry machine reservation system.

## Features
- Displays current machine availability.
- Simulates machine reservation for a student.
- Uses `datetime` for timestamps and `time` for execution pauses.

## Requirements
- Python 3.x
- Libraries: `datetime`, `time` (built-in)
