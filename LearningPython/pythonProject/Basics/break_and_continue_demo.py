# break
x = 0
y = 0
while x <= 10:
    print(x)
    x = x + 1
    print("parent while")
    while y < 5:
        print(y)
        break
        print("inner loop")
print("out of while loop")

# Continue
# x = 0
# y = 0
# while x <= 10:
#     print(x)
#     x = x + 1
#     print("parent while")
#     while y < 5:
#         print(y)
#         y = y+ 1
#         continue
#         print("inner loop")
# print("out of while loop")


# else
# x = 0
# while x <= 10:
#     print(x)
#     x = x + 1
#     if x == 5:
#         break
# else:
#     print("out of while loop")
