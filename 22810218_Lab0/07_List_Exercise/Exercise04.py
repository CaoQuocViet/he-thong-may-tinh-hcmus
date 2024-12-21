# Concatenate two lists in the following order
# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
# Expected output:

# ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
new_list = []
for i in range(len(list1)):
    for j in range(len(list2)):
        new_list.append(list1[i] + list2[j])
print(new_list)

# Output
# ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']