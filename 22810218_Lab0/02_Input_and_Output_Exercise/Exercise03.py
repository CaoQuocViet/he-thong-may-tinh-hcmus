# Convert Decimal number to octal using print() output formatting

def decimal_to_octal(decimal):
    return oct(decimal)

# Get input from the user
decimal = int(input("Enter a decimal number: "))
print("Converting", decimal, "to octal")
print("Result is:", decimal_to_octal(decimal))

# decimal = 8
# print('%o' % decimal)
