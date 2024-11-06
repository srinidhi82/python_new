def process_order(order):
    match order:
        case {"type": "regular", "items": items, "customer": customer}:
            print(f"Processing regular order for {customer} with items: {items}")
        
        case {"type": "expedited", "items": items, "customer": customer, "delivery_speed": speed}:
            print(f"Processing expedited order for {customer} with items: {items} at {speed} speed")
        
        case {"type": "bulk", "items": items, "customer": customer, "discount": discount}:
            print(f"Processing bulk order for {customer} with items: {items} and discount: {discount}%")
        
        case {"type": "special_request", "items": items, "customer": customer, "note": note}:
            print(f"Processing special request order for {customer} with items: {items} and note: {note}")
        
        case _:
            print("Unknown order type. Unable to process.")

# Example orders
order1 = {"type": "regular", "items": ["apple", "banana"], "customer": "Alice"}
order2 = {"type": "expedited", "items": ["book"], "customer": "Bob", "delivery_speed": "fast"}
order3 = {"type": "bulk", "items": ["chair", "table"], "customer": "Charlie", "discount": 10}
order4 = {"type": "special_request", "items": ["flowers"], "customer": "Diana", "note": "Handle with care"}

process_order(order3)

