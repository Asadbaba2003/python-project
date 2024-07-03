#
#def is_sorted(arr):
    # Check if the given list is sorted
    #for i in range(len(arr) - 1):
   #     if arr[i] > arr[i + 1]:
  #          return False
 #   return True

#arr = [2, 2, 5, 4, 3]
#arr.sort()
#print(arr)
#print(is_sorted(arr))
def is_sorted(lst):
    if len(lst) < 2:
        return True

    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False

    return True


# Example usage:
my_list = [1, 2, 3, 4, 5]
print(is_sorted(my_list))  # Output: True

my_list = [5, 4, 3, 2, 1]
print(is_sorted(my_list))  # Output: False



