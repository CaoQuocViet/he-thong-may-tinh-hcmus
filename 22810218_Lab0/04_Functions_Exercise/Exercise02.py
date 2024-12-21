# Create a function with variable length of arguments
# Write a program to create function func1() to accept a variable length of arguments and print their value.

def func1(*args):
    for arg in args:
        print(arg)

func1(1, 2, 3, 4, 5)
func1("Hello", "World", "Python")