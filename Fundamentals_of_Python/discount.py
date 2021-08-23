if price >= 300:
    price = price* 0.7  # (1 - 0.3)
elif price >= 200:
    price = price * 0.8  # (1 - 0.2)
elif price >= 100:
    price = price* 0.9  # (1 - 0.1)
elif price < 100 and price >= 0:
    price = price * 0.95  # (1 - 0.05)