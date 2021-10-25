# coding=gbk
# sort方法对元素排列顺序的修改是永久性的
cars = ['bmw','audi','toyota','subaru']
# 按字母顺序进行打印
cars.sort()
print(cars)
# 按字母顺序相反的顺序打印
cars.sort(reverse = True)
print(cars)
# sorted方法可以保留列表原来的排列顺序，同时以特定的排列顺序呈现它们
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)
# 倒着打印列表
# 方法reverse永久性的修改列表元素排列顺序，但可随时恢复到原有顺序，只需再次调用reverse即可
cars.reverse()
print(cars)
# len方法可以获取列表长度
print(len(cars))
