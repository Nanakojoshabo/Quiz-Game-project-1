#Add two numbers
a=6
b=5
c=a+b
print(c)

#square root of numbers
import math
print(math.sqrt(36))

#random number
import random
number = random.randint(1,10)
print(f"Random number: {number}")

#multiplicatio n table
num = int(input("Enter a new number: "))
print(f"\nMultiplication table of {num}:\n")
for i in range(1,11):
    print(f"{num} x {i} = {num * i}")

#calendar
import calendar
print(calendar.month(2025,6))

#pyramid pattern
rows = 5

for i in range(1, rows + 1):
    # Print spaces
    print(" " * (rows - i), end="")
    
    # Print stars
    print("*" * (2 * i - 1))

    # Original list
my_list = [10, 20, 30, 40, 50, 60, 70]

# Slice from index 2 to 5 (excluding index 5)
sliced_list = my_list[2:5]

# Print the sliced list
print("Original list:", my_list)
print("Sliced list (index 2 to 4):", sliced_list)

# Sample dictionary
my_dict = {'apple': 10, 'banana': 5, 'orange': 7, 'mango': 2}

# Sorting by value
sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))

# Display result
print("Dictionary sorted by value (ascending):")
print(sorted_dict)
