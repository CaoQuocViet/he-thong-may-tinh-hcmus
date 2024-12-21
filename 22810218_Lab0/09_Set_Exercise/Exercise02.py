# Return a new set of identical items from two sets

# Given:
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}

# Expected output:
# {40, 50, 30}

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
temp_set = set1.intersection(set2)
print(temp_set)

# {40, 50, 30}