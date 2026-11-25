# ================================================================================
# Gileana Hannah G. Saguil
# 8 - Sampaguita
#=================================================================================

# Activity 2 - School Canteen Order Manager

orders = []

for i in range (1,6):
    order = input(f"Enter order {i}: ")
    orders.append(order)

print("Original Orders:")
print(orders)

add_order = input("Enter additional order: ")
orders.append(add_order)
print("Updated Orders:")
print(orders)

prio_order = input("Enter prio order: ")
orders.insert(0, prio_order)
print("Updated Orders:")
print(orders)

look_item = input("Search for an order: ")
if look_item in orders:
    print(f"Number of Occurrences: {orders.index(look_item)}")
    print(f"First Index: {orders.index(look_item)}")
else:
    print("Order not found")

stop_order = input("Enter order to cancel: ")
if stop_order in orders:
    orders.remove(stop_order)
print("Updated Orders:")
print(orders)

remove_order = orders.pop
print(f"Last order removed: {remove_order}")

orders.sort()

print("===== FINAL ORDER REPORT =====")
print(f"Orders: {orders}")
print(f"Total Remaining orders: {len(orders)}")