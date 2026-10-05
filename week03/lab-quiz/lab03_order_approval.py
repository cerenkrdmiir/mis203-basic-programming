try:
    order_amount = float(input("Enter order amount (TRY): "))
    available_stock = int(input("Enter available stock: "))
    requested_quantity = int(input("Enter requested quantity: "))
    is_member_input = input("Is the customer a member? (y/n): ").strip().lower()
except ValueError:
    print("Error: Please enter valid numerical values.")
    exit()

is_member = is_member_input == 'y'

if requested_quantity <= 0:
    print("Order Rejected: Invalid order quantity.")
elif requested_quantity > available_stock:
    print("Order Rejected: Insufficient stock.")
else:
    if order_amount >= 500 and is_member:
        discount = order_amount * 0.10
        final_price = order_amount - discount
        print("Order Approved: Member discount applied (10% off).")
        print(f"Final Price: {final_price:.2f} TRY")
    else:
        final_price = order_amount
        print("Order Approved: Standard order processed without discount.")
        print(f"Final Price: {final_price:.2f} TRY")
