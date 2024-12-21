# Print characters from a string that are present at an even index number
# Write a program to accept a string from the user and display characters that are present at an even index number.

def even_index_characters(str):
    for i in range(len(str)):
        if i % 2 == 0:
            print(str[i])

# Get input from the user
str = input("Enter a string: ")
print("Original string is", str)
print("Printing only even index characters:")
even_index_characters(str)