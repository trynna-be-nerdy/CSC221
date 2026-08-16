from math import ceil                     

# Painting a Wall Program
# Calculates the cost to paint a wall. Paint required is based on wall area,
# and the total cost includes paint plus 7% sales tax.


#  Step 1: read inputs and compute wall area 
# Read wall height, wall width, and cost of one paint can (all floats)
wall_height = float(input("Enter wall height (ft): "))
wall_width = float(input("Enter wall width (ft): "))
paint_cost_per_can = float(input("Enter cost of one paint can ($): "))

# Wall area = height * width
wall_area = wall_height * wall_width
print(f"Wall area: {wall_area:.1f} sq ft")

#  Step 2: compute paint needed 
# One gallon of paint covers 350 square feet
paint_needed = wall_area / 350
print(f"Paint needed: {paint_needed:.3f} gallons")

#  Step 3: compute number of 1-gallon cans needed 
# Round up to the nearest whole gallon since cans are sold whole
cans_needed = ceil(paint_needed)
print(f"Cans needed: {cans_needed} can(s)")

# Step 4: compute paint cost, sales tax, and total cost 
paint_cost = cans_needed * paint_cost_per_can   # cost of the cans bought
sales_tax = paint_cost * 0.07                    # 7% sales tax on the paint
total_cost = paint_cost + sales_tax              # total the customer pays

print(f"Paint cost: ${paint_cost:.2f}")
print(f"Sales tax: ${sales_tax:.2f}")
print(f"Total cost: ${total_cost:.2f}")
