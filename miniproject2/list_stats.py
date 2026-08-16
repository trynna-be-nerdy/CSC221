# List Program
# Calculates minimum, maximum, mean, median, mode, and checks whether the
# list of values is a palindrome.

# Explain to the user exactly what to type before asking for input
print('This program calculates statistics for a list of whole numbers.')
print('Type your numbers on one line, separated by spaces, then press Enter.')
print('Example: 1 2 3 2 1')
print()

# Keep asking until the user types at least one valid whole number.
# This prevents the program from crashing on blank input or on words.
values = []
while len(values) == 0:
    user_input = input('Enter your numbers: ')
    values = []
    valid = True

    # Split the line into pieces and convert each piece to an integer
    for piece in user_input.split():
        try:
            values.append(int(piece))
        except ValueError:
            print(f'"{piece}" is not a whole number. Please try again.')
            valid = False
            break

    # Throw out the whole line if any piece was not a number
    if not valid:
        values = []
    elif len(values) == 0:
        print('You did not enter any numbers. Please try again.')

print()

# Step 1: Find minimum and maximum values
minimum = min(values)
maximum = max(values)

# Step 2: Calculate mean as the sum of all values divided by the number of values
mean = sum(values) / len(values)

# Step 3: Check if palindrome, meaning values are the same from front to back and back to front.
# the output should be "true" or "false".
is_palindrome = values == values[::-1]

# Step 4: sort the values in ascending order.
# After sorting the list, find the median, which is the value located in the middle of the list.
# if the list has an odd number of values or
# the average of the middle two values, if the list has an even number of values
sorted_values = sorted(values)
n = len(sorted_values)
mid = n // 2
if n % 2 == 1:
    median = sorted_values[mid]
else:
    median = (sorted_values[mid - 1] + sorted_values[mid]) / 2

# Step 5: Identify the mode of the list, after you sorted in ascending order.
# The mode is the value that appears most frequently. Assume that only one mode exists.
# Hint: Use a loop to process each list element, looking for the longest sequence of identical values.
mode = sorted_values[0]
current_value = sorted_values[0]
current_count = 1
best_count = 1
for value in sorted_values[1:]:
    if value == current_value:
        current_count += 1
    else:
        current_value = value
        current_count = 1
    if current_count > best_count:
        best_count = current_count
        mode = current_value

# Display the results
print(f'Values: {values}')
print(f'Minimum: {minimum}')
print(f'Maximum: {maximum}')
print(f'Mean: {mean:.2f}')
print(f'Palindrome: {"true" if is_palindrome else "false"}')
print(f'Median: {median}')
print(f'Mode: {mode}')
