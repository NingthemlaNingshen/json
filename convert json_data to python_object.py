import json
json_obj =  '{ "Name":"David", "Class":"I", "Age":6 }'
python_obj = json.loads(json_obj)
print("\nJSON data:")
print(python_obj)
print("\nName: ",python_obj["Name"])
print("Class: ",python_obj["Class"])
print("Age: ",python_obj["Age"]) 

# import json
# x =  '{ "name":"John", "age":30, "city":"New York"}'
# y = json.loads(x)
# # the result is a Python dictionary:
# print(y["age"])

import json
json_obj='{"name":"david","class":5}'
py_obj=json.loads(json_obj)
print(py_obj["name"])


# import json 

# data = """{ 
#     "Name": "Jennifer Smith", 
#     "Contact Number": 7867567898, 
#     "Email": "jen123@gmail.com", 
#     "Hobbies":["Reading", "Sketching", "Horse Riding"] 
#     }"""
    
# r = json.loads( data )    
# # the result is a Python dictionary: 
# print( r )
# print(type(r))
# print(type(data))


# import json 
# data = {
#     "name": "RM",
#     "place": "KOREA",
#     "skills": [
#         "RAPPER",
#         "DANCING"
#     ],
#     "email": "xyz@gmail.com",
#     "projects": [
#         "PERMISSION TO DANCE",
#         "SPRING DAY"
#     ]
# }
# with open( "data_file.json" , "w" ) as write:
#     json.dump( data , write )
# with open("data_file.json", "r") as read_content:
#     print(json.load(read_content))



# import json
# f=open("my_json_data.json","r")
# a=json.load(f)
# print(a)
# print(type(a))
# f.close()



