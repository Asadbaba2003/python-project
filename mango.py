import pymango
myclient = pymango.MangoClient("mongodb://localhost:27017/")
print(myclient.list_databse_names())