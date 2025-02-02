def calc_numbers(*args):
    total = 0
    for values in args:
        total +=values
    return total
    
print(calc_numbers(3,6,8))
print(calc_numbers(6,8))