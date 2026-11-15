# Practice Set 2: Functions, Strings & Lists

Assignment 59 TechDestination / PSEB Bootcamp. Two Python programs built with functions, string methods and lists.

## Features

### Task 1  Student Result Card Generator (`student_result_card.py`)

- Takes a student's name, roll number and marks in 5 subjects.
- Validates marks (0–100) and roll number (digits only).
- Cleans the name with `strip()` and `title()`.
- Calculates total marks, percentage and grade (A / B / C / D / F).
- Result is **Fail** if any subject is below 40, even with a high total.
- Prints a formatted result card.

### Task 2 Shopping Bill Calculator (`shopping_bill_calculator.py`)

- Takes at least 3 items with price and quantity, stored in lists.
- Calculates the subtotal from items, prices and quantities.
- Applies a **10% discount** if the subtotal is above 5000, otherwise **5%**.
- Adds **5% GST** on the discounted amount.
- Prints a formatted bill with subtotal, discount, GST and grand total.

## Project Structure

```text
practice-set-2-functions-strings-lists/
├── README.md
├── student_result_card.py
└── shopping_bill_calculator.py
```

## How to Run

Requires Python 3.8 or newer. No external packages needed.

```bash
python student_result_card.py
python shopping_bill_calculator.py
```

## Sample Output

Student Result Card (from the brief's example):

```text
---------- STUDENT RESULT CARD ----------
Name        : Ali Raza
Roll Number : 101
Marks       : 85, 90, 78, 88, 82
Total Marks : 423/500
Percentage  : 84.60%
Grade       : A
Result      : Pass
-----------------------------------------
```

Shopping Bill (from the brief's example):

```text
Subtotal    : 3020.00
Discount    : 151.00
GST (5%)    : 143.45
Grand Total : 3012.45
```

## Testing

Both programs were tested against the brief's example outputs, which reproduce exactly. Edge cases also verified:

| Case | Result |
| --- | --- |
| Any subject below 40 | Fail |
| Subtotal above 5000 | 10% discount |
| Fewer than 3 items | Rejected |
| Invalid marks / inputs | Rejected and re-asked |

## Technologies

- Python 3 functions, string methods (`strip`, `title`, `isdigit`), lists and formatted output.
