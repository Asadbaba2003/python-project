def has_duplicates(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] == lst[j]:
                return True
    return False

# Example usage:
my_list = [1, 2, 3, 4, 5]
print(has_duplicates(my_list))  # Output: False

my_list = [1, 2, 3, 3, 4, 5]
print(has_duplicates(my_list))  # Output: True
