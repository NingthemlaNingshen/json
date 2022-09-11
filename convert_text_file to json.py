# Q7.Text file data ko json file data mai convert karo,jaise ki neeche diya hai?

# Example:

# Input :-


# Text.txt:-  
#  Name Abhishek
#  Designation CEO of navgurukul
#  Gender male
#  Age 29
# Visualize
# Output:-

# Json_file.json:-


# {
#     “Name”: “Abhishek”,
#     “Designation”: “CEO of      navgurukul”,
#     “Gender”:”male”,
#     “Age”: “29”
#     }



import json
d={}
with open("Text.txt") as f:
    for i in f:
        x , y = i.strip().split(None,1)
        d[x]=y.strip()
f1=open("Json.json","w")
json.dump(d, f1,indent=3,sort_keys=False)
f1.close()


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

# s=0
# for i in range(0,1001):
#     s=s+i
# print(s)


