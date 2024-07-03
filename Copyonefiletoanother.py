fp=open("csea.txt","r")
fp1=open("csea1.txt","w+")
if fp:
    print("file opened successfully")
for i in fp:
    fp1.write(i)
print("file is copy succesfully")
fp1.seek(0,0)
content=fp1.read()
#print(content)
fp.close()
fp1.close()