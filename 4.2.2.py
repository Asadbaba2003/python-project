fp=open("world.txt",  "w")
if fp:
    print("successfully opened")
    fp.write("i")
    fp.write("a")
    fp.write(" ")
    fp.close()