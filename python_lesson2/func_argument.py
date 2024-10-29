def sub_one(x):
    return x/4

def new_func(lst, func):

    #eturn [func(x) for x in lst]
    return [func(x) for x in lst]


my_list = [20,40,80,96]

new_list_output = new_func(my_list, sub_one)

print(f"The newly created list is {new_list_output}")