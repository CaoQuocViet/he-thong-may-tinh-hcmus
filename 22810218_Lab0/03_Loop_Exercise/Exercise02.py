# Print the following pattern
# Write a program to print the following number pattern using a loop.

# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5

i = 1
j = 1
while i <= 5:
    while j <= i:
        print(j, end=" ")
        j += 1
    print()
    i += 1
    j = 1

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5