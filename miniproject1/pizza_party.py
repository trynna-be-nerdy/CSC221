import math

# Pizza Party Program
# Calculates the cost of hosting pizza parties on Friday, Saturday and Sunday.
# Each party includes: pizza cost, sales tax, delivery charge, and a total.

days = ['Friday', 'Saturday', 'Sunday']  # party names, one per night
weekend_total = 0.0  # running total across all parties

print('Pizza Party Program — enter details for each night.')
print('For each night, type three values separated by spaces: people slices_per_person pizza_cost')
print('Example:  10 2.5 12.99')
print()

for day in days:
    # Read number of people, average slices per person, and cost per pizza
    parts = input(f'{day} Night (people slices_per_person pizza_cost): ').split()
    if len(parts) != 3:
        print("Please enter exactly three values: people slices_per_person pizza_cost")
        continue
    people, slices_per_person, pizza_cost = parts
    people = int(people)
    slices_per_person = float(slices_per_person)
    pizza_cost = float(pizza_cost)

    # Total slices needed, rounded up to whole pizzas (8 slices per pizza)
    num_pizzas = math.ceil(people * slices_per_person / 8)

    # Cost of all pizzas
    pizza_total = num_pizzas * pizza_cost

    # Sales tax (7%) on pizza cost
    tax = pizza_total * 0.07

    # Delivery charge (20% of cost including tax)
    delivery = (pizza_total + tax) * 0.20

    # Total cost including pizza, tax and delivery
    order_total = pizza_total + tax + delivery

    # Add this party's total to the weekend running total
    weekend_total += order_total

    # Output results for this party
    print(f'{day} Night Party')
    print(f'{num_pizzas} Pizzas: ${pizza_total:.2f}')
    print(f'Tax: ${tax:.2f}')
    print(f'Delivery: ${delivery:.2f}')
    print(f'Total: ${order_total:.2f}')
    print()

# Output total for all parties
print(f'Weekend Total: ${weekend_total:.2f}')
