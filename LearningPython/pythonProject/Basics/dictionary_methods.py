# get
# demo_dict2 = {"qa":"testurl", "uat":"uaturl","prod":"produrl"}
# # print(demo_dict2.get("uat"))
# # print(demo_dict2.keys())
# # print(demo_dict2.items())
# # print(demo_dict2.values())
# # print(demo_dict2.pop("prod"))
# # print((demo_dict2.popitem()))
# # demo_copy = demo_dict2.copy()
# demo_dict2.update({"stag":"stagurl"})
# print(demo_dict2)

dict = {"qa":"testurl", "uat":"uaturl","prod":"produrl"}
dict.update({"dsprm":"stag"})
print(dict)