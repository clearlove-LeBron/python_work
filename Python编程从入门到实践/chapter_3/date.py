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
# 删除这位嘉宾
date_list.remove('chenhuilin')
# 添加新的嘉宾
date_list.append('yujing')
# 再次打印消息
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
# 向三个不同的位置添加三位嘉宾
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
# 指出你邀请了多少名嘉宾
message = "I have invited " + str(len(date_list)) + " girls to my party"
print(message)
# 删除嘉宾至只剩两位
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
# 让名单变为空
del date_list[1]
del date_list[0]
print(date_list)
