# Problem 2: Finance
# This program computes the future value of an investment for each
# year from 1 to 20, given an investment amount and annual interest rate.


def futureInvestmentValue(investmentAmount, monthlyInterest, years):
    # Convert years to months since interest is compounded monthly
    numberOfMonths = years * 12
    # Apply the future value formula
    return investmentAmount * (1 + monthlyInterest) ** numberOfMonths


# Get the investment amount and annual interest rate from the user
investmentAmount = float(input('Enter the investment amount: '))
annualInterest = float(input('Enter the annual interest rate in percent: '))

# Convert annual interest percent to a monthly interest rate
monthlyInterest = annualInterest / 100 / 12

# Print a table of future values for years 1 through 20
print('Years\tFuture Value')
for years in range(1, 21):
    futureValue = futureInvestmentValue(investmentAmount, monthlyInterest, years)
    print(f'{years}\t{futureValue:.2f}')
