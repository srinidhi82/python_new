def total_addition(*numbers):
    addition = 0
    for number in numbers:
        addition += number
    return addition

print(total_addition(1,2,3))

def fun(*args):return args

print(fun(1, 2, 3))
print(fun(23, 24))

def calc(*int):
    result = 1
    for x in int:
        result *= x
    return result

print(calc(1,2,3,4,5))

def function(var1=2, var2=4):
    var2 = 6
    var1 = 5
    print(var1, var2)

function(10, 20)