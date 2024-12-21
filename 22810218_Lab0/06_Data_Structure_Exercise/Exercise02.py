# Remove and add item in a list
# Write a program to remove the item present at index 4 and add it to the 2nd position and at the end of the list.

list1 = [34, 54, 67, 89, 11, 43, 94]
print("Original list: ", list1)
# Remove the item at index 4
item = list1.pop(4)
print("List After removing element at index 4: ", list1)
# Add the item at index 2
list1.insert(2, item)
print("List after Adding element at index 2: ", list1)
# Add the item at the end of the list
list1.append(item)
print("List after Adding element at last: ", list1)
# Output: [34, 54, 11, 67, 89, 43, 94, 11]