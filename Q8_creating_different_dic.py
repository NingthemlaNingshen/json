import json
file="file_dic_to_json.txt"
c=["Name","Disgnation","age","salary"]
d={}
with open(file) as f1:
    x=1
    for i in f1:
        a=list( i.strip().split(None,4))
        print(a)
#         b="emp"+str(x)
#         j=0
#         dic={}
#         while j<len(c):
#             dic[c[j]]=a[j]
#             j=j+1
#         d[b]=dic   
#         x=x+1
# with open("dic_to_json.json","w") as f:
#     json.dump( d , f , indent=5) 
    
