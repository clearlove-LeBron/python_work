#  coding=gbk
# �����ӡ��ֵ5
for value in range(1,5):
	print(value)
# ʹ��list�����ɽ�һϵ������ת�����б�
numbers = list(range(1,5))
print(numbers)
# range��������ָ������
# ��ӡ1-10��ż��
even_numbers = list(range(2,11,2))
print(even_numbers)
# ����һ���б�����1-10��ƽ��
squares = []
for value in range(1,11):
	square = value ** 2
	squares.append(square)
print(squares)
# ʹ���б����ʵ�ִ���һ���б�����1-10��ƽ��
pingfangs = [value**2 for value in range(1,11)]
print(pingfangs)
# ʹ��һ��forѭ����ӡ����1-20
for value in range(1,21):
	print(value)
# ����һ���б����1-1000000���ٽ���Щ���ִ�ӡ����,�ҳ����ֵ,��Сֵ,����1000000�����ֵĺ�
number_list = [value for value in range(1,1000001)]
for number in number_list:
	print(number)
print("The largest number is " + str(max(number_list)))
print("The smallest number is " + str(min(number_list)))
print("The sum of the numbers is " + str(sum(number_list))) 
