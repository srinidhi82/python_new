def print_info(*args, **kwargs):
    print("Arguments:", args)
    print("Keyword Arguments:", kwargs)

print_info('name',1,34,80.9,'blaaah', name='Bob', age= 30)

def concatenate_strings(separator, *args):
    print("Args value", args)
    return separator.join(args)
    

result = concatenate_strings(" - ", "Python", "is", "great")
print(result)  # Output: Python, is, great

def print_student_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_student_info(name="Alice", age=20, major="Computer Science")