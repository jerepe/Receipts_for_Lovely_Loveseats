# COMMENTS ARE ADDed FROM MY WILL, HELPS ME VISUALISE WHAT I'M DOING :)

# ITEMS IN STORE
# Loveseat description
lovely_loveseat_description = """Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep.
Red or white."""

# Loveseat unit price
lovely_loveseat_price = 254.00

# Settee description
stylish_settee_description = """Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep.
Black."""

# Settee price
stylish_settee_price = 180.50

# lamp description
luxurious_lamp_description = """Luxurious Lamp. Glass and iron. 36 inches tall.
Brown with cream shade."""

#lamp price
luxurious_lamp_price = 52.15

# taxes
sales_tax = 0.088

# CUSTOMERS REGISTRY
# customer one status before buying
customer_one_total = 0

# customer one status
customer_one_itemization = ""

# customer one total due update
customer_one_total += lovely_loveseat_price

# customer one status update
customer_one_itemization += lovely_loveseat_description + "\n"

# customer one buys lamp, amount due update
customer_one_total += luxurious_lamp_price

# customer one status update
customer_one_itemization += luxurious_lamp_description + "\n"

# customer's shopping done, tax calculation
customer_one_tax = customer_one_total * sales_tax

# adding taxes to customer total
customer_one_total += customer_one_tax

# RECIPE PRINTING
print()
print("Customer One Items:" + "\n")
print(customer_one_itemization)
print("Customer One Total:"+ "\n")
print(customer_one_total)
print()
