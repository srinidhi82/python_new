
#import function1 as f1
from function1 import number_calc_avg
def add(a:int, b:int)-> int:
    return a + b

calc = number_calc_avg(8)
print(f"value is {calc:.2f}")
