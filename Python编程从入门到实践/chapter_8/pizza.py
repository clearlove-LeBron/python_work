# coding=gbk
def make_pizza(*toppings):
	"""����Ҫ����������"""
	print("\nMaking the pizza with following toppings:")
	for topping in toppings:
		print("- " + topping)
make_pizza('pepperoni')
make_pizza('mushrooms','green papers','extra cheese')
