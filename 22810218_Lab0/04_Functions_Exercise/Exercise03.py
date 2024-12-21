# Return multiple values from a function
# Write a program to create function calculation() such that it can accept two variables and calculate addition and subtraction. Also, it must return both addition and subtraction in a single return call.

def calculation(a, b):
    return a + b, a - b

result = calculation(10, 5)

print("Addition: ", result[0])
print("Subtraction: ", result[1])

print("-------------------")

print(result)

print("-------------------")

res2, res3 = calculation(10, 5)
print("Addition: ", res2)
print("Subtraction: ", res3)

print("-------------------")

print(res2, res3)