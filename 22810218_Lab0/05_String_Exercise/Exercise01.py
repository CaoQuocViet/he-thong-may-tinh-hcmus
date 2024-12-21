# Append new string in the middle of a given string
# Given two strings, s1 and s2. Write a program to create a new string s3 by appending s2 in the middle of s1.

def append_string(s1, s2):
    middle = len(s1) // 2
    return s1[:middle] + s2 + s1[middle:]
    
# Get the input from the user
s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")
print("The new string is: ", append_string(s1, s2))