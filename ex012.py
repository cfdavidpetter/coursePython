price = float(input('Which is price of product?'))
discount = price - ((price / 100) * 5)
print('The product price is ${} in promotion with 5% discount it will cost ${:.2f}'.format(price, discount))