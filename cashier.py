def main():
	# write code here
	items_list = []
	item = input("Item (enter \"done\" when finished): ")
	while item != "done":
		price = input("Price: ")
		quan = input("Quantity: ")
		dict = {"name": item, "price": price, "quantity": quan}
		items_list.append(dict)
		item = input("Item (enter \"done\" when finished): ")
	total_price = 0
	print("\n-------------------\nreceipt\n-------------------")
	for i in items_list:
		price = float(i["quantity"])*float(i["price"])
		total_price += price
		print("%s %s %.3fKD"%(i["quantity"],i["name"],price))
	print("-------------------\nTotal Price: %.3fKD"%(total_price))





if __name__ == '__main__':
	main()
