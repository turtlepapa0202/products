# 讓使用者重複輸入要買的商品，直到q，最後把所有商品的清單印出來
# 若要讓使用者也處理價格，要怎麼處理? (使用二維清單)
# 清單中還有清單

import os # operating system

# 讀取檔案
def read_file(filename):
	products = []
	with open(filename, 'r') as f:
	# with open('products.csv', 'r', encoding = 'utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue
			name, price = line.strip().split(',')
			# r = (line.strip().split(','))
			# name = r[0]
			# price = r[1]
			# print(r)
			products.append([name, price])
	return products

# 讓使用者輸入
def user_input(products):
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
	return products

# 把商品價格印出來
def print_products(products):
	for p in products:
		print(p[0], '的價格是', p[1])

# 寫入檔案
def write_file(filename, products):
	with open(filename, 'w', encoding = 'utf-8') as f:
		# f.write('商品' + ',' + '價格' + '\n') # 直接寫法
		f.write('商品,價格\n')
		for p in products:
			f.write(p[0] + ',' + p[1] + '\n')

# 簡化程式，小list裝入大list
# s_product = [prod_name, price]
# products.append(s_product)

# 更簡化程式
# products.append([prod_name, price])

# 試著使用function

def main():
	filename = 'products.csv'
	if os.path.isfile(filename):
		print('yeah！ 找到檔案了')
		products = read_file(filename)
	else:
		print('找不到檔案...')
	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)
main()
