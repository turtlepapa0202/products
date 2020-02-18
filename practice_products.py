# 讓使用者重複輸入要買的商品，直到q，最後把所有商品的清單印出來
# 若要讓使用者也處理價格，要怎麼處理? (使用二維清單)
# 清單中還有清單

products = []
# s_product = [] # 注意小清單要再回圈裏面(自己想想why~)

while True:
	prod_name = input('請輸入要買的商品: ')
	if prod_name == 'q':
		break
	price = input('請輸入購買的價格: ')
	s_product = []
	s_product.append(prod_name.strip())
	s_product.append(price.strip())
	products.append(s_product)
print(products)
print(products[0])
print(products[0][0])

# 簡化程式，小list裝入大list
s_product = [prod_name, price]
products.append(s_product)

# 更簡化程式
products.append([prod_name, price])
