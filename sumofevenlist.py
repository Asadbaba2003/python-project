lst = list(map(int, input().split()))
even_sum = sum(x for x in lst if x % 2 == 0)
print(even_sum)
