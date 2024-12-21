# Turn every item of a list into its square
# Given a list of numbers. write a program to turn every item of a list into its square.

# Given:

# numbers = [1, 2, 3, 4, 5, 6, 7]
# Expected output:

# [1, 4, 9, 16, 25, 36, 49]

numbers = [1, 2, 3, 4, 5, 6, 7]
squared_numbers = [number ** 2 for number in numbers]
print(squared_numbers)

# Output
# [1, 4, 9, 16, 25, 36, 49]