import sys

# Income Tax Program
# Calculates U.S. income tax owed from wages, taxable interest, unemployment
# compensation, filing status (1=single, 2=married), and taxes withheld.
# Short form may only be used when AGI is below $120,000.

# --- Step 1: read inputs and compute AGI ---
# All five values are entered on one line, separated by spaces, as integers:
#   wages  taxable_interest  unemployment  status  taxes_withheld
print("Enter 5 whole numbers on one line, separated by spaces:")
print("  wages  taxable_interest  unemployment  status(1=single,2=married)  taxes_withheld")
print("Example:  20000 23 500 1 400")
wages, interest, unemployment, status, withheld = input().split()
wages = int(wages)
interest = int(interest)
unemployment = int(unemployment)
status = int(status)
withheld = int(withheld)

# Adjusted Gross Income = wages + interest + unemployment
agi = wages + interest + unemployment
print(f"AGI: ${agi:,}")

# Taxpayers may only use this short form if AGI is not above $120,000
if agi > 120000:
    print("Error: Income too high to use this form")
    sys.exit()

# --- Step 2: deduction and taxable income ---
# Any status that is not 1 or 2 defaults to 1 (single)
if status != 1 and status != 2:
    status = 1

# Deduction depends on filing status
if status == 1:
    deduction = 12000        # single
else:
    deduction = 24000        # married
print(f"Deduction: ${deduction:,}")

# Taxable income cannot be negative
taxable_income = agi - deduction
if taxable_income < 0:
    taxable_income = 0
print(f"Taxable income: ${taxable_income:,}")

# --- Step 3: federal tax from the bracket tables ---
# Tax is computed as a double, then rounded to the nearest whole dollar.
if status == 1:
    # Single filer brackets
    if taxable_income <= 10000:
        tax = 0.10 * taxable_income
    elif taxable_income <= 40000:
        tax = 1000 + 0.12 * (taxable_income - 10000)
    elif taxable_income <= 85000:
        tax = 4600 + 0.22 * (taxable_income - 40000)
    else:
        tax = 14500 + 0.24 * (taxable_income - 85000)
else:
    # Married filer brackets
    if taxable_income <= 20000:
        tax = 0.10 * taxable_income
    elif taxable_income <= 80000:
        tax = 2000 + 0.12 * (taxable_income - 20000)
    else:
        tax = 9200 + 0.22 * (taxable_income - 80000)

tax = round(tax)   # round to nearest whole dollar
print(f"Federal tax: ${tax:,}")

# --- Step 4: amount due or refund ---
# A negative amount due means the taxpayer gets a refund.
amount_due = tax - withheld
if amount_due < 0:
    print(f"Tax refund: ${-amount_due:,}")
else:
    print(f"Tax due: ${amount_due:,}")
