# Remove first n characters from a string
# Write a program to remove characters from a string starting from zero up to n and return a new string.

def remove_chars(str, n):
    return str[n:]

# Get input from the user
str = input("Enter a string: ")
n = int(input("Enter the number of characters to remove: "))

# Call the function and print the result
print("Original string is:", str)
print("Removing the first", n, "characters")
print("Result is:", remove_chars(str, n))