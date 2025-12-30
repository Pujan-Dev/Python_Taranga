# coor = (10,201,12,2,3,4)
# coor[0]=20
# print(coor)
# alist = [1,2,3,4]
# alist[0]=20
# print(alist)

# aset = {1,2,3}
# print(aset)
# print(type(aset))
# print(4 in aset)
# print(2 in aset)

# adict = {
#     "name":"pujan",
#     "course":"python"
# }
# for key,value in adict.items():
#     print(key,value)
# print(adict["name"])


# text ="Python"
# nums= [1,2,3,4,5,6]
# print(text[:3])
# print(text[0:2])
# print(nums[:3])
# print(nums[1:3])

# alist = [1,2,7,3,6,5]
# for i in range(len(alist)):
#     for j in range(i,len(alist)):
#         if alist[i] > alist[j]:
#             # temp = alist[i]
#             # alist[i]= alist[j]
#             # alist[j] = temp
#             alist[i],alist[j] = alist[j],alist[i]
# print(alist)

# alpa = ["a","b","c"]
# userinput = input("Enter a letter")
# for index, value in enumerate(alpa):
#     if userinput.lower() == value:
#         print(index,value)
#     else:
#         pass

# def sum(a,b):
#     return a,b, a+b
# a,b,res = sum(1,2)
# print(a,"+",b, "=",res)
# def user_info(name,age):
#     print("name",name,"age",age)

# user_info("hari",20)
# user_info(22,"shyam")
# user_info(age = 12, name = "ram")

# def total(*args):
#     print(len(args))
#     product = 1
#     for i in range(len(args)):
#         product = product*args[i]
#     print(args)
#     print(type(args))
#     return product

# print(total(1,3,4))

def profile(**kwargs):
    print(type(kwargs))
    print(kwargs)
    for key,value in kwargs.items():
        print(key,value)
profile(name="pujan",role="student",dep="department")