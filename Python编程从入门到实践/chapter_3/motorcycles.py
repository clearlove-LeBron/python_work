# coding=gbk
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
# ��ָ��λ���б����Ԫ��
motorcycles.insert(0,'ducati')
print(motorcycles)
# ɾ���б�Ԫ��
del motorcycles[0]
print(motorcycles)
# ʹ��pop����ɾ��Ԫ��
poped_motorcycle = motorcycles.pop()
print(motorcycles)
print("The last motorcycle I owned was a " + poped_motorcycle.title()+".")
# ʹ��pop���������б��κ�λ�õ�Ԫ��
first_owned = motorcycles.pop(0)
print(motorcycles)
print("The first motorcycle I owned was a " + first_owned.title()+".")
# ʹ��remove��������ֵɾ��Ԫ��
# ��ʹ��append�������һЩԪ��
motorcycles.append('zhangsan')
motorcycles.append('lisi')
motorcycles.append('wangmazi')
print(motorcycles)
motorcycles.remove('lisi')
print(motorcycles)
