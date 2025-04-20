#!/usr/bin/env python3
"""
simple_calculator.py
A tiny interactive calculator that shows how to raise, catch, and
handle exceptions in Python.
"""

class QuitCommand(Exception):
    """Raised when the user types 'q' to quit the program."""
    pass


def parse_number(text: str) -> float:
    """Convert user input to a float or raise a ValueError."""
    if text.strip().lower() == "q":
        raise QuitCommand("User chose to quit.")
    try:
        return float(text)
    except ValueError as err:
        # enrich the built‑in ValueError with context and re‑raise it
        raise ValueError(f"'{text}' is not a valid number.") from err


def calculate(a: float, b: float, op: str) -> float:
    """Perform the requested operation or raise a ValueError."""
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b == 0:            # detect an illegal operation ourselves
            raise ZeroDivisionError("Cannot divide by zero!")
        return a / b
    else:
        raise ValueError(f"Unsupported operator: {op!r}")


def main() -> None:
    print("=== Simple Calculator ===")
    print("Enter two numbers and an operator (+ - * /). Type 'q' to exit.\n")

    while True:
        try:
            a_text = input("First number: ")
            a = parse_number(a_text)

            b_text = input("Second number: ")
            b = parse_number(b_text)

            op = input("Operator (+ - * /): ").strip()

            result = calculate(a, b, op)   # may raise ZeroDivisionError / ValueError
        except QuitCommand:
            print("Good‑bye!")
            break                          # graceful exit
        except ZeroDivisionError as zde:
            print(f"Error: {zde}")         # specific handler
            continue
        except ValueError as ve:
            print(f"Input error: {ve}")    # catch all other bad inputs
            continue
        else:
            # This runs only if *no* exception happened in the try‑block
            print(f"Result: {result}\n")
        finally:
            # Executes every iteration, regardless of success or failure
            print("-" * 30)

if __name__ == "__main__":
    main()
