
def read_data(file_name, L):
	ifile = open(file_name, 'r')
	ifile.readline()

	line = ifile.readline()
	while line:
		L.append(line.strip())
		line = ifile.readline()

	ifile.close()

def compute_discount(products, discounts, best_prices):
	for product in products:
		product_fields = product.split(',')
		product_price = float(product_fields[1])

		best_price = product_price
		best_date = '2022-11-03'

		for discount in discounts:
			discount_fields = discount.split(',')
			discount_pct = float(discount_fields[1])
			discount_min = float(discount_fields[2])

			if product_price >= discount_min:
				discounted_price = ( product_price - ( product_price * ( discount_pct / 100 ) ) )
				discounted_price = round(discounted_price, 2)

				if discounted_price < best_price:
					best_price = discounted_price
					best_date = discount_fields[0]
		best_prices.append([product_fields[0], best_price, best_date])

discounts = []
products = []
best_prices = []

read_data('discounts.csv', discounts)
read_data('products.csv', products)

compute_discount(products, discounts, best_prices)

for item in best_prices:
	# print("The best price on " + item[0] + " was " + str(item[1]) + " on " + item[2])
	print(f"The best price on {item[0]} was {item[1]} on {item[2]}")






