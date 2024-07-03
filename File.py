'''

open()
read()
readline()
write()
writeline()
close()
fseek()
tell()

'''

fp = open("csea.txt","w")
if fp:
    print("file is created successfully")

fp.writelines(" hi student welcome to cmr engineering college\n today classes are done\n today python class is on files")


fp.close()