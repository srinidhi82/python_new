#x = 30
x = 0
while x < 5:
    print(f" The value of x is {x}")
    x +=1

else:
    print("The value of x is less than 5")


my_string = "Johnny"

# continue keyword
'''Improving code readability: It helps avoid deep nesting of if statements, making the logic clearer and easier to read.
Efficient processing: Skipping unnecessary work in loops helps in optimizing performance.'''
for letters in my_string:
    if letters == 'h':
        continue
    print(letters)
    
# Skipping even numbers
for i in range(1, 12):
    if i % 2 ==0:
        continue
    print(i)

# Pass

x = 100
while x > 100:
    pass
print("End")
   

# break

x = 0
while x < 5:
    if x ==3:

        break
    print(x)
    x +=1