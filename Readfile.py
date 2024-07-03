fp = open("csea.txt", "r")
if fp:
    print("File is opened successfully")
fp.seek(10, 0)
for i in fp:
    print(i)
'''content = fp.read(5)
print(content)
content=fp.readline()
print(content)'''
fp.close()