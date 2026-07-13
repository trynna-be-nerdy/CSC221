import math

# Carpet Sale Program
# Calculates cost of replacing carpet for one or more rooms/orders.
# Each order includes: carpet cost (with 20% waste), labor cost, sales tax, and total cost.

total_sales = 0.0  # running total across all orders

num_orders = 3  # number of orders to process

for order_num in range(1, num_orders + 1):
    # Read carpet price per sq ft, room width, and room length for this order
    price_per_sqft, width, length = input().split()
    price_per_sqft = float(price_per_sqft)
    width = int(width)
    length = int(length)

    # Calculate room area in square feet
    area = width * length

    # Carpet cost includes an extra 20% for waste
    carpet_cost = area * price_per_sqft * 1.20

    # Labor cost is $0.75 per actual square foot (no waste added)
    labor_cost = area * 0.75

    # Sales tax (7%) applies to carpet + labor cost combined
    tax = (carpet_cost + labor_cost) * 0.07

    # Total cost for this order
    order_cost = carpet_cost + labor_cost + tax

    # Add this order's cost to the running total
    total_sales += order_cost

    # Output results for this order
    print(f'Order #{order_num}')
    print(f'Room: {area} sq ft')
    print(f'Carpet: ${carpet_cost:.2f}')
    print(f'Labor: ${labor_cost:.2f}')
    print(f'Tax: ${tax:.2f}')
    print(f'Cost: ${order_cost:.2f}')
    print()

# Output total sales for all orders
print(f'Total Sales: ${total_sales:.2f}')
