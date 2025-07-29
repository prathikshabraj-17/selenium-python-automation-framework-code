from operator import index

demo_dict = {}
demo_dict1 = {1:10, 2:20, 3:45, 6:60}
demo_dict2 = {"qa":"testurl", "uat":"uaturl"}
demo_dict3 = {'qa':34,3:"uaturl"}

print(type(demo_dict))
print(demo_dict1[2])
print(demo_dict2['uat'])
demo_dict2['prod'] =  "produrl","uat"
demo_dict2[1] = 56

print(demo_dict2)
demo_dict2.pop(1)
print(demo_dict2)
