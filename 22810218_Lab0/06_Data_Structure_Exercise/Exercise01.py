# Create a list by picking an odd-index items from the first list and even index items from the second
# Given two lists, l1 and l2, write a program to create a third list l3 by picking an odd-index element from the list l1 and even index elements from the list l2.

list1 = [3, 6, 9, 12, 15, 18, 21]
list2 = [4, 8, 12, 16, 20, 24, 28]
res = list()
for i in range(len(list1)):
    if i % 2 != 0:
        res.append(list1[i])
for i in range(len(list2)):
    if i % 2 == 0:
        res.append(list2[i])
print(res)
# Output: [6, 12, 18, 4, 12, 20, 28]

# list1 = [3, 6, 9, 12, 15, 18, 21]
# list2 = [4, 8, 12, 16, 20, 24, 28]
# res = list()

# odd_elements = list1[1::2]
# print("Element at odd-index positions from list one")
# print(odd_elements)

# even_elements = list2[0::2]
# print("Element at even-index positions from list two")
# print(even_elements)

# print("Printing Final third list")
# res.extend(odd_elements)
# res.extend(even_elements)
# print(res)
