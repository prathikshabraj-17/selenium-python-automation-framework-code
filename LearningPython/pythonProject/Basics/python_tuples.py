demo_tuple = (1,2,3,4,5)
demo_tuple1 = ("Mysore","Delhi","Delhi","Dallas","Texas","Banglore")
demo_tuple2 = (True,False,False,True)
demo_tuple3 = (True,2,"delhi",23.45)
# print(demo_tuple[0])
# print(len(demo_tuple1))
# print(len(demo_tuple2))
# print(type(demo_tuple1))
# print(type(demo_tuple3))
# print(demo_tuple1.count("Delhi"))
# print(demo_tuple1.index("Dallas"))
# print(type(demo_tuple3))
for x in demo_tuple:
    print(x)

joined_tuple = demo_tuple1+demo_tuple2+demo_tuple
print(joined_tuple)
