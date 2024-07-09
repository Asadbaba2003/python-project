n = int(input())
s = 0
temp = n
while temp:
    s += (temp % 10) ** 3
    temp //= 10
if s == n:
    print("Armstrong")
else:
    print("Not Armstrong")
