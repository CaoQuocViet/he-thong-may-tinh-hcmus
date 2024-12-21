# Print the sum of the current number and the previous number
# Write a program to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number.

def sum_of_previous_number():
    previous_number = 0
    for i in range(10):
        sum = previous_number + i
        print("Current Number", i, "Previous Number ", previous_number, " Sum: ", sum)
        previous_number = i

sum_of_previous_number()