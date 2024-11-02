def original_list(old_box, new_box):
    while old_box:

        new_box_list = old_box.pop()
        print(f"The new box after modifying is {new_box_list}")
        new_box.append(new_box_list)

def show_new_box(new_box):
    for items in new_box:
        print(f"The list of items in {items} is here: ")

old_box = ['blue','orange', 'yellow', 'white']
new_box =[]

original_list(old_box, new_box)
show_new_box(new_box)
        
                
