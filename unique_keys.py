import json
j_str='{"a":  1,"a":  2,"a":  3, "a": 4,   "b": 1, "b": 2}'
p_obj=json.loads(j_str)
a=json.dumps(p_obj)
print("Unique Key in a python object:-",p_obj)
print("Unique Key in a json object:-",a)

print(type(a))
print(type(p_obj))



  