# coding=gbk
# sort������Ԫ������˳����޸��������Ե�
cars = ['bmw','audi','toyota','subaru']
# ����ĸ˳����д�ӡ
cars.sort()
print(cars)
# ����ĸ˳���෴��˳���ӡ
cars.sort(reverse = True)
print(cars)
# sorted�������Ա����б�ԭ��������˳��ͬʱ���ض�������˳���������
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)
# ���Ŵ�ӡ�б�
# ����reverse�����Ե��޸��б�Ԫ������˳�򣬵�����ʱ�ָ���ԭ��˳��ֻ���ٴε���reverse����
cars.reverse()
print(cars)
# len�������Ի�ȡ�б���
print(len(cars))
