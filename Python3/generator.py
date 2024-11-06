def generate_cust_ids(customer_id=1):
    #customer_id = start
    while True:
        yield f"CUST -- {customer_id}"
        customer_id+=1

cust_ids = generate_cust_ids()
print(next(cust_ids))
print(next(cust_ids))
print(next(cust_ids))
print(next(cust_ids))
print(next(cust_ids))

print(next(cust_ids))

