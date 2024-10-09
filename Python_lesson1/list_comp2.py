#list_1 = [1, 2, 3, 4, 5]
#list_comp = [ i for i in list_1 ]
#print(list_comp)


# first is traditional for and if logic to see if budget meets discount
discounted_price = [665.0, 1140.0, 1425.0, 1116.25]

budget = int(input('Enter the Budget in dollars: '))
within_budget = []

'''
for x in discounted_price:
    if x<= budget:
        within_budget.append('Yes')
    else:
        within_budget.append('No')
print(within_budget)

'''

# Using list comprehension to do this

afford_phone = ['Yes' if x<=budget else 'No' for x in discounted_price]
print(afford_phone)
print(min(discounted_price))