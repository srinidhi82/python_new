# Get the desired input from the user
n = int(input("Enter an integer: "))

# Initialize a variable i to 0
i = 0

# Use a while loop to iterate while i is less than or equal to n
while i <= n:
    # Check if i is even
    if i % 2 == 0:
        # Print the value of i if it is even
        print(i)
    # Increment the value of i by 1
    i += 1