# Write a program print duplicate element present in the list

my_list = [1, 2, 3, 2, 4, 5, 1, 6, 7, 5]

duplicates = []

for item in my_list:
    if my_list.count(item) > 1 and item not in duplicates:
        duplicates.append(item)

print("Duplicate elements are:", duplicates)
