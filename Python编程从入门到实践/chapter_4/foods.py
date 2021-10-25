# coding=gbk
my_foods = ['pizza','falafel','carrot cake']
# 若使用friend_foods = my_foods,实际上是让新变量friend_foods关联到my_foods的列表,此时，这两个变量指同一个列表
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
