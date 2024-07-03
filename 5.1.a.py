
r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))


a = []

for i in range(r):
    row = []
    for j in range(c):
        row.append(int(input("Enter the value: ")))
    a.append(row)


b = []
print("Enter the elements of the second matrix:")
for i in range(r):
    row = []
    for j in range(c):
        row.append(int(input("Enter the value: ")))
    b.append(row)

for i in range(r):
    for j in range(c):
        c[i][j] = a[i][j] + b[i][j]


print("The resulting matrix after addition is:")
for i in range(r):
    for j in range(c):
        print(c[i][j], end=" ")
    print()