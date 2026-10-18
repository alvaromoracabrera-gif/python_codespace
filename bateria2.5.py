date = input("Date: ")
day, month, year = date.split("/")
print(f"Date: {day.zfill(2)}/{month.zfill(2)}/{year}")

product = input("Product: ")
price = float(input("Unit price: "))
quantity = int(input("Quantity: "))

euros = int(price)
cents = round((price - euros) * 100)
total = price * quantity

print(f"Euros: {euros} · Cents: {cents:02d}")
print(f"{product} {price:09.2f} {quantity:03d}                  {total:011.2f}")
