# CSC 221

Coursework for CSC 221 (Introduction to Programming in Python). Each mini project is a folder of standalone Python scripts. Every script is run directly from the command line and reads its input interactively from the keyboard.

## Requirements

- Python 3.6 or newer (the scripts use f-strings)
- No third-party packages — standard library only (`math`, `sys`)

## Running a program

```bash
python miniproject1/carpet_sale.py
```

Each program prints instructions describing what to type before it asks for input.

## Mini Project 1 — input, calculations, and control flow

Console programs that read numeric input, apply formulas, and format currency output.

| File | Description |
| --- | --- |
| [painting_wall.py](miniproject1/painting_wall.py) | Computes wall area, gallons of paint needed (350 sq ft per gallon, rounded up to whole cans), paint cost, 7% sales tax, and total. |
| [pizza_party.py](miniproject1/pizza_party.py) | For Friday, Saturday, and Sunday: computes pizzas needed (8 slices each, rounded up), cost, 7% tax, 20% delivery charge, and a weekend total. |
| [carpet_sale.py](miniproject1/carpet_sale.py) | Processes 3 carpet orders. Carpet cost includes 20% extra for waste, labor is $0.75 per actual sq ft, 7% tax applies to both, plus a running total of all sales. |
| [grade_calculator.py](miniproject1/grade_calculator.py) | Converts homework, quiz, midterm, and final points into percentages (capped at 100%), applies UG/G/DL weighting, and reports the course average and letter grade. |
| [income_tax.py](miniproject1/income_tax.py) | Computes AGI, standard deduction by filing status, taxable income, federal tax from the bracket tables, and the amount due or refunded. Exits if AGI exceeds $120,000. |

### Input formats

- **painting_wall.py** — three prompts: wall height, wall width, cost per can.
- **pizza_party.py** — one line per night: `people slices_per_person pizza_cost` (e.g. `10 2.5 12.99`).
- **carpet_sale.py** — one line per order: `price_per_sqft width length` (e.g. `12.50 10 15`).
- **grade_calculator.py** — first line: `UG`, `G`, or `DL`. Second line: `homework quizzes midterm final` (e.g. `600.0 300.0 120.0 185.0`).
- **income_tax.py** — one line of five whole numbers: `wages interest unemployment status withheld`, where status is `1` for single or `2` for married (e.g. `20000 23 500 1 400`).

## Mini Project 2 — lists, dictionaries, functions, and classes

Programs built around data structures and reusable functions.

| File | Description |
| --- | --- |
| [schedule_info.py](miniproject2/schedule_info.py) | Looks up a course's room, instructor, and meeting time from three parallel dictionaries. Input is normalized to uppercase and invalid course numbers are reported. |
| [finance.py](miniproject2/finance.py) | Prints a table of future investment values for years 1–20 using monthly compounding, via a `futureInvestmentValue()` function. |
| [list_stats.py](miniproject2/list_stats.py) | Reads a list of whole numbers and reports minimum, maximum, mean, median, mode, and whether the list is a palindrome. Re-prompts on invalid or empty input. |
| [contact_info.py](miniproject2/contact_info.py) | Stores contacts as a list of dictionaries and provides functions to print a full table, a phone-only table, look up a phone by full name, look up an address by first name, and list cities/states. |
| [bank_account.py](miniproject2/bank_account.py) | Defines a `BankAccount` class with checking and savings balances, supporting deposits, withdrawals (rejected when they exceed the balance), transfers to savings, and a display method. |

### Input formats

- **schedule_info.py** — a course number such as `CS101` (case-insensitive).
- **finance.py** — investment amount, then annual interest rate as a percent.
- **list_stats.py** — whole numbers on one line, separated by spaces (e.g. `1 2 3 2 1`).
- **contact_info.py** — no input; runs a built-in test program against the sample contacts.
- **bank_account.py** — amount to withdraw from checking, then amount to withdraw from savings.

## Repository layout

```
csc221/
├── miniproject1/
│   ├── carpet_sale.py
│   ├── grade_calculator.py
│   ├── income_tax.py
│   ├── painting_wall.py
│   └── pizza_party.py
└── miniproject2/
    ├── bank_account.py
    ├── contact_info.py
    ├── finance.py
    ├── list_stats.py
    └── schedule_info.py
```
