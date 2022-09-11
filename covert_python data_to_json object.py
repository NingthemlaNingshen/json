# import json 
      
# # Data to be written 
# dictionary ={ 
#   "id": "04", 
#   "name": "sunil", 
#   "department": "HR"
# } 
      
# # Serializing json  
# json_object = json.dumps(dictionary, indent = 4) 
# print(json_object)




# import json
    
# # Data to be written
# dictionary ={
#     "name" : "sathiyajith",
#     "rollno" : 56,
#     "cgpa" : 8.6,
#     "phonenumber" : "9976770500"
# }
    
# with open("sample.json", "w") as outfile:
#     json.dump(dictionary, outfile)


import json
f=open("dump.json","w")
a={"name" : "Ningthemla","rollno" : 13,"height" : 4.5,"phonenumber" : 8730896921}
json.dump(a, f,indent=4)

f.close()