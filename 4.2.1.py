def remove_duplicate(li):
    unique_list = []
    duplicate_list = []

    for i in li:
        if i not in unique_list:
            unique_list.append(i)
        else:
            duplicate_list.append(i)
    return unique_list

li = [1, 2, 3, 3, 4, 4, 5, 6, 7, 9, 0]
print("Original list:", li)
print("List with duplicates removed:", remove_duplicate(li))
