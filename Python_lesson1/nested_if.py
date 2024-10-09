def check_conditions(a, b, c):
    if a > 0:  # Check if the first integer is positive
        if b % 2 == 0:  # Check if the second integer is even
            if c % 3 == 0:  # Check if the third integer is divisible by 3
                print("All conditions are satisfied.")
            else:
                print("Conditions are not satisfied.")
        else:
            print("Conditions are not satisfied.")
    else:
        print("Conditions are not satisfied.")

check_conditions(10, 89, 99)
