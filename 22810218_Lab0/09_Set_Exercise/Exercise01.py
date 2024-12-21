# Add a list of elements to a set
# Given a Python list, Write a program to add all its elements into a given set.

# Given:
# sample_set = {"Yellow", "Orange", "Black"}
# sample_list = ["Blue", "Green", "Red"]

# Expected output:
# Note: Set is unordered.

# {'Green', 'Yellow', 'Black', 'Orange', 'Red', 'Blue'}

sample_set = {"Yellow", "Orange", "Black"}
sample_list = ["Blue", "Green", "Red"]
sample_set.update(sample_list)
print(sample_set)

# {'Green', 'Yellow', 'Black', 'Orange', 'Red', 'Blue'}