# Position Arguement
# Keyword argument
# Required argument
# Optional argument


# Position Arguement
def sub_demo(x,y):
    return x-y

z = sub_demo(4,8)
print(z)

# Optional argument
# def sub_demo(x=5,y=6):
#     return x-y
# print(sub_demo(6,9))
# print(sub_demo(8))
# print(sub_demo())

# Keyword argument
def sub_demo(x=9,y=6):
    return x-y
print(sub_demo(8,6))
print(sub_demo(8))
print(sub_demo())
print(sub_demo(y=10))
