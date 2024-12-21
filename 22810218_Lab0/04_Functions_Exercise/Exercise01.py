# Create a function in Python
# Write a program to create a function that takes two arguments, name and age, and print their value.

# Function to print name and age
def print_name_age(name, age):
    print("Name: ", name)
    print("Age: ", age)

# Get name and age from user
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print_name_age(name, age)