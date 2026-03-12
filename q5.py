#Input cost price and discount percentage
cost_price = float(input("Enter cost prize of book:"))
discount = float(input("Enter discount percentage:"))

#calculate discount amount
discount_amount = (cost_price * discount) / 100

#calculate selling price
selling_price = cost_price - discount_amount

#Display result
print("Discount Amount =",discount_amount)
print("Selling price+",selling_price)