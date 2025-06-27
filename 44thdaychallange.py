# format specifiers = {:flags} format a value based on what flags are inserted

# .(number)f = round to that many decimal places
# :(number) = allocate that many spaces
# :0(number) = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma separator
# :% = percentage format

price1 = 3000.14159
price2 = -9870.65
price3 = 1200.34
print(f"Price is ${price1:+,.2f}")
print(f"Price is ${price2:+,.2f}")
print(f"Price is ${price3:+,.2f}")