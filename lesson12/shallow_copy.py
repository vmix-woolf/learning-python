from copy import copy, deepcopy

my_list = [1, 2, {"name": "Gupalo Vasyl", "sex": {"male": True}}]
copy_list = deepcopy(my_list)
copy_list[2]["age"] = 30
copy_list[2]["sex"]["male"] = False
copy_list.append(4)
print(my_list)
print(copy_list)
