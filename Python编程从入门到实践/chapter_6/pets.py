# coding=gbk
# 遍历列表中的字典
Eric = {'type':'dog','owner':'zhangyuechuan'}
Alice = {'type':'cat','owner':'yuyingying'}
Bob = {'type':'bird','owner':'wangfengxia'}
pets = [Eric,Alice,Bob]
for pet in pets:
	print("\nThis pet is a " + pet['type'] + " and its owner is " + pet['owner'])
