# Accept numbers from a user
# Write a program to accept two numbers from the user and calculate multiplication

def multiply_numbers(a, b):
    return a * b

# Get input from the user
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# Call the function and print the result
print("Multiplying", a, "and", b)
print("Result is:", multiply_numbers(a, b))