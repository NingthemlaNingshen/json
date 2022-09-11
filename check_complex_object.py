# Json string ko check karo ki bo complex object contain karti hai 
# # ya nahi?


# import json
# def is_complex_num(objct):
#     if '__complex__' in objct:
#         return complex(objct['a'], objct['b'])
#     return objct

# complex_object =json.loads('{"__complex__": true, "a": 4, "b": 5}', object_hook = is_complex_num)
# simple_object =json.loads('{"real": 4, "img": 3}', object_hook = is_complex_num)
# print("Complex_object: ",complex_object)
# print("Without complex object: ",simple_object)


import json
def complex_num(obj):
    if '__complex__' in obj:
        return complex(obj['a'],obj['b'])
    return obj
complex_object=json.loads('{"__complex__":true,"a":4,"b":5}',object_hook=complex_num)
print(complex_object)


 

        