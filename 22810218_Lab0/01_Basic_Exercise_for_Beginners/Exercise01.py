# Calculate the multiplication and sum of two numbers
# Given two integer numbers, return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.

def multiplication_or_sum(num1, num2): 
    product = num1 * num2
    if product <= 1000:
        return product
    else:
        return num1 + num2

# Get input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Call the function and print the result
result = multiplication_or_sum(num1, num2)
print("The result is", result)