# coding=gbk
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
# 向指定位置列表添加元素
motorcycles.insert(0,'ducati')
print(motorcycles)
# 删除列表元素
del motorcycles[0]
print(motorcycles)
# 使用pop方法删除元素
poped_motorcycle = motorcycles.pop()
print(motorcycles)
print("The last motorcycle I owned was a " + poped_motorcycle.title()+".")
# 使用pop方法弹出列表任何位置的元素
first_owned = motorcycles.pop(0)
print(motorcycles)
print("The first motorcycle I owned was a " + first_owned.title()+".")
# 使用remove方法根据值删除元素
# 先使用append方法添加一些元素
motorcycles.append('zhangsan')
motorcycles.append('lisi')
motorcycles.append('wangmazi')
print(motorcycles)
motorcycles.remove('lisi')
print(motorcycles)
