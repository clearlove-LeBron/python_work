# coding=gbk
my_foods = ['pizza','falafel','carrot cake']
# ��ʹ��friend_foods = my_foods,ʵ���������±���friend_foods������my_foods���б�,��ʱ������������ָͬһ���б�
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
