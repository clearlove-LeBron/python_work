# coding=gbk
date_list = ['wangfengxia','yuyingying','yanghui','wangxiang','chenhuilin']
message = date_list[0].title() + ", would you have a date with me?"
print(message)
message = date_list[1].title() + ", would you have a date with me?"
print(message)
message = date_list[2].title() + ", would you have a date with me?"
print(message)
message = date_list[3].title() + ", would you have a date with me?"
print(message)
message = date_list[4].title() + ", would you have a date with me?"
print(message)
message = date_list[4].title() + " can't come to the date for some reasons."
print(message)
# ɾ����λ�α�
date_list.remove('chenhuilin')
# ����µļα�
date_list.append('yujing')
# �ٴδ�ӡ��Ϣ
message = date_list[0].title() + ", would you have a date with me?"
print(message)
message = date_list[1].title() + ", would you have a date with me?"
print(message)
message = date_list[2].title() + ", would you have a date with me?"
print(message)
message = date_list[3].title() + ", would you have a date with me?"
print(message)
message = date_list[4].title() + ", would you have a date with me?"
print(message)
message = "I have found a bigger table for our date."
print(message)
# ��������ͬ��λ�������λ�α�
date_list.insert(0,'wuguibing')
date_list.insert(3,'wangzihang')
date_list.append('lihuanhuan')
message = date_list[0].title() + ", would you have a date with me?"
print(message)
message = date_list[1].title() + ", would you have a date with me?"
print(message)
message = date_list[2].title() + ", would you have a date with me?"
print(message)
message = date_list[3].title() + ", would you have a date with me?"
print(message)
message = date_list[4].title() + ", would you have a date with me?"
print(message)
message = date_list[5].title() + ", would you have a date with me?"
print(message)
message = date_list[6].title() + ", would you have a date with me?"
print(message)
message = date_list[7].title() + ", would you have a date with me?"
print(message)
# ָ���������˶������α�
message = "I have invited " + str(len(date_list)) + " girls to my party"
print(message)
# ɾ���α���ֻʣ��λ
message = "I'm sorry to tell all of you that the table is not ready so that I can only invite two girls!"
print(message)
poped_girl = date_list.pop()
message = poped_girl.title() + ", I'm sorry to tell you that you're out of my party."
print(message)
poped_girl = date_list.pop()
message = poped_girl.title() + ", I'm sorry to tell you that you're out of my party."
print(message)
poped_girl = date_list.pop()
message = poped_girl.title() + ", I'm sorry to tell you that you're out of my party."
print(message)
poped_girl = date_list.pop()
message = poped_girl.title() + ", I'm sorry to tell you that you're out of my party."
print(message)
poped_girl = date_list.pop()
message = poped_girl.title() + ", I'm sorry to tell you that you're out of my party."
print(message)
poped_girl = date_list.pop()
message = poped_girl.title() + ", I'm sorry to tell you that you're out of my party."
print(message)
message = date_list[0].title() + ",I'm glad to tell you that I'm still going to invite you."
print(message)
message = date_list[1].title() + ",I'm glad to tell you that I'm still going to invite you."
print(message)
# ��������Ϊ��
del date_list[1]
del date_list[0]
print(date_list)
