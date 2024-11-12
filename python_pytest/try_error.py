def calc_days(my_input) -> None:
    try:
        # Attempt to convert my_input to an integer if it's not already one
        total_days: int = int(my_input) * 365
        print(f"Total days: {total_days}")
        
    except ValueError:
        print("Bad Input: invalid literal for int()")
    except TypeError:
        print("Bad Input: Input must be an integer.")