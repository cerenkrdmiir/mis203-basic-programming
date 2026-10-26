def calculate_subtotal(unit_price, quantity):
    return unit_price * quantity

def calculate_discount_rate(subtotal):
    if subtotal >= 500:
        return 0.10
    else:
        return 0.0

def calculate_shipping_fee(subtotal):
    if subtotal >= 500:
        return 0.0
    else:
        return 50.0

def calculate_final_total(unit_price, quantity):
    subtotal = calculate_subtotal(unit_price, quantity)
    discount_rate = calculate_discount_rate(subtotal)
    discount_amount = subtotal * discount_rate
    shipping_fee = calculate_shipping_fee(subtotal) 
    final_total = (subtotal - discount_amount) + shipping_fee
    return final_total

assert calculate_final_total(100, 4) == 450.0
assert calculate_final_total(100, 6) == 540.0
assert calculate_subtotal(50, 3) == 150.0

print("All assert checks passed successfully!")

order1_price = 120.0
order1_qty = 5
result1 = calculate_final_total(order1_price, order1_qty)
print(f"Order 1 Final Total: {result1} TL")
order2_price = 90.0
order2_qty = 3
result2 = calculate_final_total(order2_price, order2_qty)
print(f"Order 2 Final Total: {result2} TL")
