item_info = 'Mug 18 18'

item_tokens = item_info.split()
item = item_tokens[0]
quantity = item_tokens[1]
price = item_tokens[2]

print(item, 'stock:', quantity)
print('Price:', price)
