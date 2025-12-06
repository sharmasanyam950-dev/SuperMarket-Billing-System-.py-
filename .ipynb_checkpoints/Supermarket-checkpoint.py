print("==================== Supermarket Management System ==================")
item_name = []
item_quantity = []
item_price = []
item_total=[]

while True:
    name = input("Enter the item name: ")
    quantity = int(input("Enter the item Quantity: "))
    price = float(input("Enter the item price:"))
    total = quantity * price

    item_name.append(name)
    item_quantity.append(quantity)
    item_price.append(price)
    item_total.append(total)

    choice = input("Do you want to add more items? (yes/no): ").lower( )
    if choice =='no':
        break

    

print("\n==================== Bill Invoice ==================")
print("{:<15} {:<10} {:<10} {:<10} ".format("Name", "Quantity", "Price", "Total"))
print("----------------------------------------")
subtotal = sum(item_total)

if subtotal >= 5000:
        discount = subtotal * 0.20
elif subtotal >= 2500:
        discount = subtotal * 0.10
elif subtotal >= 1000:
        discount = subtotal * 0.05
else:
        discount = 0

        
final_total = subtotal - discount 

for i in range(len(item_name)):
    print("{:<15} {:<10} {:<10.2f} {:<10.2f}".format(item_name[i], item_quantity[i], item_price[i], item_total[i]))

print("------------------------------------------")
print(f"Subtotal: ₹{subtotal:.2f}")
print(f"Discount: ₹{discount:.2f}")
print(f"Final Total: ₹{final_total:.2f}")
print("Thank you for shopping with us!")

    

