def read_product_data():
    products = {}
    while True:
        product_name = input("Enter product name (or 'n' to stop): ")
        if product_name.lower() == 'n':
            break
        price = float(input("Enter price: "))
        products[product_name] = price
    return products

def get_product_price(products, product_name):
    if product_name in products:
        print(f"The price of {product_name} is: ${products[product_name]}")
    else:
        print(f"{product_name} not found in the data.")

def get_products_in_price_range(products, min_price, max_price):
    matching_products = []
    for product_name, price in products.items():
        if min_price <= price <= max_price:
            matching_products.append(product_name)
    if matching_products:
        print(f"Products within price range ${min_price} - ${max_price}:")
        for product in matching_products:
            print(product)
    else:
        print("No products found within the specified price range.")

# Read product data
products = read_product_data()

# Allow user to get price of a product
product_name = input("Enter product name to get the price: ")
get_product_price(products, product_name)

# Allow user to enter price range and get matching products
min_price = float(input("Enter minimum price: "))
max_price = float(input("Enter maximum price: "))
get_products_in_price_range(products, min_price, max_price)
