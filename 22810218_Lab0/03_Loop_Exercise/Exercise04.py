# Write a program to print multiplication table of a given number

# Get input from the user
number = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(number, "x", i, "=", number * i)
    i += 1

# Enter a number: 5
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# 5 x 4 = 20
# 5 x 5 = 25
# 5 x 6 = 30
# 5 x 7 = 35
# 5 x 8 = 40
# 5 x 9 = 45
# 5 x 10 = 50