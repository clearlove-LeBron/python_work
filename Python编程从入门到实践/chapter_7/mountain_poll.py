# coding=gbk
responses = {}
#����һ����־��ָ�������Ƿ����
polling_active = True
while polling_active:
	#��ʾ���뱻�����ߵ����ֺͻش�
	name = input("\nWhat's your name?")
	response = input("\nWhich mountain would you like to climb someday?")
	#���𰸾�洢���ֵ���
	responses[name] = response
	#�����Ƿ�����Ҫ�������
	repeat = input("Would you like to let another person respond?(yes/no)")
	if repeat == 'no':
		polling_active = False
#�����������ʾ���
print("\n---- Poll Results ----")
for name,response in responses.items():
	print(name + " would like to climb " + response + ".")
