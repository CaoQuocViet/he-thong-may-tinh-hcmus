# Arrange string characters such that lowercase letters should come first
Given string contains a combination of the lower and upper case letters. Write a program to arrange the characters of a string so that all lowercase letters should come first.

def arrange_string(s):
    lower = ""
    upper = ""
    for char in s:
        if char.islower():
            lower += char
        else:
            upper += char
    return lower + upper

# Get the input from the user
s = input("Enter the string: ")
print("The new string is: ", arrange_string(s))