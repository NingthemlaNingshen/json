import json
dic={
    '4': 5, 
    '6': 7, 
    '1': 3, 
    '2': 4}
f=open("sorted_keys.json","w")
json.dump(dic, f ,indent=4,sort_keys=True)
f.close()
