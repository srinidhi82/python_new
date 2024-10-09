def func(a):
  print(a)
A = [0,1,2,3]
func(A)

def say(message, times):
    print(message*times)
say("How are you", 2)

# function to display attributes of phone

def iphone_attributes():
    price = 1400
    RAM = 12
    storage = 512
    

    print(f"The attributes of phone are size is {RAM}, cost is {price} and space is{storage}")

iphone_attributes()

def phone_details(brand, storage, RAM, price):
   print(f"The attributes of phone are size is {RAM}, cost is {price} and space is {storage} and the make is {brand}")

phone_details('Nokia', 256, 8, 900)


def phone_discount(discount):
   
   price = 1000
   discount_price = price - price * (discount/100)
   return discount_price
   
new_price = phone_discount(15)
print(new_price)

def mths(a, b):
 print(a + b)
 print(a - b)
 print(a * b)
 print(a // b)
 
mths(9, 5)

def sq():
 for i in range(1, 11):
     print(i ** 2)
sq()

def num(x):
 y = x * x
 z = y + 5
 return z

print(num(5))

def power(a, b):
 return a ** b
power(7,2)