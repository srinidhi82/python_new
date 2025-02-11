def calculate_tip(price: float) -> float:
    if price >= 150:
        return 25.0
    elif price >= 50:
        return price * 0.25
    return price * 0.2
tips = calculate_tip(25)
print(tips)