def restaurant_order(customer_name,customer_table,*dishes,**special_requests):
    print(f"Customer Name: {customer_name}")
    print(f"Customer Table: {customer_table}")
    print(f"Dishes: {dishes}")
    if special_requests:
        print("\nSpecial Requests:")
        for request, detail in special_requests.items():
            print(f"{request}: {detail}")


restaurant_order("John",5,"Biryani","Kabab","Naan",drink="wine",dessert="Ice Cream",starter='fries')