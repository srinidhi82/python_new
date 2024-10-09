
def main():
    x = get_int()
    print(f"The value of x is {x}")

    a = get_div_error()

def get_int():
    while True:
        try:
            return int(input("Enter a numerical value: "))
        except ValueError:
            pass

def get_div_error():
   try:
       result = 10/0
   except ZeroDivisionError:
       print("Cannot divide by zero")
   except ValueError:
       print("bad Input")

main()
            
     