# coding=gbk

with open('���̼�Dashboard.html','w',encoding='utf-8') as html_file:
	html_file.write('<html><head><title>���̼�Dashboard</title>' + 
		'<meta charset="utf-8"></head><body>\n')
	for svg in [
			'���̼�����ͼ(��).svg','���̼۶����任����ͼ(��).svg',
			'���̼�����ƽ��ֵ(��).svg','���̼�����ƽ��ֵ(��).svg',
			'���̼����ھ�ֵ(��).svg'
	]:
		html_str = '	<object type="image/svg+xml" data="{0}"' 
		html_str += ' height=500></object>\n'
		html_file.write(html_str.format(svg))
	html_file.write('</body><html>')

	
