n = int(input("Enter the n value: "))
a = 0
b = 1
c = 0
if n <= 0:
    print("Enter positive number")
elif n == 1:
    print(a)
else:
    print("Fibonacci series:")
    print(a)
    print(b)
    while c < n:
        c = a + b
        print(c, end=" ")
        a = b
        b = c
