price_list = [700, 1200, 1500, 1175]
discount_new_price_list = []

for x in price_list:
    discount_price = x - (x *(5/100))
    discount_new_price_list.append(discount_price)
                    
print(discount_new_price_list)

discount_price_list = [x - (x *(5/100)) for x in price_list]
print(discount_price_list)