# Calculate the sum of all numbers from 1 to a given number
# Write a program to accept a number from a user and calculate the sum of all numbers from 1 to a given number

# For example, if the user entered 10 the output should be 55 (1+2+3+4+5+6+7+8+9+10)

# Get input from the user
number = int(input("Enter a number: "))
sum = 0
i = 1
while i <= number:
    sum += i
    i += 1
print("The sum of all numbers from 1 to", number, "is", sum)

# Enter a number: 34
# The sum of all numbers from 1 to 34 is 595