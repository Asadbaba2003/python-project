def invert_content(dic):
    invert_dic={}
    invert_dic={v:k for v,k in dic.items()}
    return invert_dic



n=int(input("enter no. of values"))
dic={}
for i in range(n):
    key=input("enter key")
    value=input("enter value")
    dic[key]=value
print(dic)
print("after inversion")
print(invert_content(dic))