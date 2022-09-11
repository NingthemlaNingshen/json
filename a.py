# dic={"a":1,"b":5,"c":2,"d":9,"e":3,"g":5}
# m=0
# c=0
# for i in dic:
#     if dic[i]>m:
#         m=dic[i]
# for j in dic:
#     if dic[j]==m:
#         c=c+1
# print(m,c)




# dic={"a":-5,"b":-5,"c":-2,"d":-1,"e":-3,"g":-5}
# a=[]
# c=0
# for i in dic :
#     a.append(dic[i])
#     m=a[0]
#     for j in a:
#         if j>m:
#             m=j
# for k in dic:
#     if dic[k]==m:
#         c=c+1
# print(m,c)


# def name(n):
#     i=0
#     b=[]
#     while i<len(n):
#         j=0
#         c=0
#         while j<len(n):
#             if n[i]==n[j]:
#                 c=c+1
#                 a=n[i]
#             j=j+1
#         i=i+1
#         if c==1:
#             b.append(a)
#     print(b[0])
# n=input("enter your chr: ")
# name(n)
# l=[-1,-2,-3,-1,-5,-1,-7]
# c=0
# m= l[0]
# print(m)
# for i in l :
#     if i>m :
#         m = i
# for j in l:
#     if j==m:
#         c=c+1
# print(m,c)
def num(n):
    i=0
    a=""
    b=""
    c="-"
    while i<len(n):
        if i<3:
            a=a+str(n[i])
        elif i>=3 and i<6:
            b=b+str(n[i])
        else:
            c=c+str(n[i])
        i=i+1
    print("("+a+")"+" "+b+c)
num("1234567890")


def phone_no(n):
    i=0
    a=""
    b=""
    c="-"
    while i<len(n):
        if i<3:
            a=a+str(n[i])
        elif i>=3 and i<6:
            b=b+str(n[i])
        else:
            c=c+str(n[i])
        i=i+1
    y="("+a+")"+" "+b+c
    return y
phone_no("1234567890")



