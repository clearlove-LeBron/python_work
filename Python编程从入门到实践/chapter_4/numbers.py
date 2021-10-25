#  coding=gbk
# 不会打印数值5
for value in range(1,5):
	print(value)
# 使用list方法可将一系列数字转换成列表
numbers = list(range(1,5))
print(numbers)
# range方法还可指定步长
# 打印1-10的偶数
even_numbers = list(range(2,11,2))
print(even_numbers)
# 创建一个列表，包含1-10的平方
squares = []
for value in range(1,11):
	square = value ** 2
	squares.append(square)
print(squares)
# 使用列表解析实现创建一个列表，包含1-10的平方
pingfangs = [value**2 for value in range(1,11)]
print(pingfangs)
# 使用一个for循环打印数字1-20
for value in range(1,21):
	print(value)
# 创建一个列表包含1-1000000，再将这些数字打印出来,找出最大值,最小值,计算1000000个数字的和
number_list = [value for value in range(1,1000001)]
for number in number_list:
	print(number)
print("The largest number is " + str(max(number_list)))
print("The smallest number is " + str(min(number_list)))
print("The sum of the numbers is " + str(sum(number_list))) 
