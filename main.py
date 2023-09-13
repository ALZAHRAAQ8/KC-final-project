print("Welcome to the Simple Shopping Cart")
basket = []
bas1=input("Enter item 1:")
bas2=input("Enter item 2:")
bas3=input("Enter item 3:") 
basket.append(bas1)
basket.append(bas2)
basket.append(bas3)

print(f"Enter item 2:{bas2}")
print(f"Enter item 3:{bas3}")
print(f"Enter item 1:{bas1}")


print("Your Shopping Cart:")
print(f"1.{bas1}")
print(f"2.{bas2}")
print(f"3.{bas3}")

print(f"total items in the cart:{len(basket)}")

index =int(input(f"Enter the index of item you want to remove (0-2):"))

basket.pop(index)


print(f"""updated shopping cart: 
      1.{basket[0]}
      2.{basket[1]}""")

price1=float(input("enter the price of 'bas1':"))
price3=float(input("enter the price of 'bas2': "))

print(f"total cost of all items: {price1 + price3} ")
