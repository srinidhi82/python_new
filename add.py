def number_calc_avg(numbers):

    """

    avoind division by zero error
    """
    if not numbers:
       return 0
    
    total = sum(numbers)
    avg = total/ len(numbers)
    return avg

list_numbers = [10,30,60,120,75,32.75,68.25]

result = number_calc_avg(list_numbers)

print(f"THe result is {result:.2f}")