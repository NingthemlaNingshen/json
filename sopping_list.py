
# phir main user se poochu ga ki kon sa item khareedna chahte ho.

# 3

# uske baad user name dega phir user se input poochege jaise ki tum kitne item chahte ho.

# 4

# phir aapka wo number of items json file se remove karna hai.

# 5

# Agar tumhe shopping items add karna hai to tumko json file main insert karna hoga.
# shopping_list:- 

# {
#     "shopping_list":{ 
#         "chaco":"15",          ##output
#         "Biscuits":"50",
#         "Diary_milk":"30",
#         "ice_cream":"20",
#          } 
# }
# part 1

# import json
# a={
#     "shopping_list":
#         { 
#             "chaco":"15",
#             "Biscuits":"50",
#             "Diary_milk":"30",
#             "ice_cream":"20",
#         } 
# }
# f=open("task.json","w")
# x=json.dump(a,f,indent=4)
# f.close()


# part2

import json
a={}
b={}
user=input("enter the items you want to buy: ")
num=int(input("enter your number: "))
for i in range(num):
    item_user=input("enter your item: ")
    amount_item=int(input("enter your number: "))
    a[item_user]=amount_item
b[user]=a
with open("sopping_list.json","w")as f:
    json.dump( b , f , indent=5)

