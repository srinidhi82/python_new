cars = ['audi', 'bmw', 'mazda', 'Mercedes', 'honda']

for index, car in enumerate(cars, start=10):
    print(index,car)



fruit_baskets = (('apple',10), ('banana',12),('orange','6'))

for index ,(fruit, quantity) in enumerate(fruit_baskets, start=1):
    print(f'Basket {index}: {fruit} - Quantity: {quantity}')