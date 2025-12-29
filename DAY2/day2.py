# alist = [1,2,3,4,5,6,9]

# for i in alist:
#     print(i)

# a= 5
# while(a!=10):
#     print(a)
#     a=a+1

# print(a)

# for i in range(1,6):
#     if i == 3:
#         break
#     print(i)

# for i  in range(1,6):
#     if i ==3 :
#         continue
#     print(i)

# for i in range(1,11):
#     if i == 5:
#         continue
#     if i == 8:
#         break
#     print(i)

fruits = ["apple"]
number = [1,2,3,4,7,5]
userinput = int(input("Enter a number:"))
found = False
for i in number:
    if userinput == i:
        found = True
        print("yes the user input is in the list",userinput)
        break
    else:
        pass
if (not found):
    print("Enter number is not in the list ")