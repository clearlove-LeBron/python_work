# coding=gbk

with open('收盘价Dashboard.html','w',encoding='utf-8') as html_file:
	html_file.write('<html><head><title>收盘价Dashboard</title>' + 
		'<meta charset="utf-8"></head><body>\n')
	for svg in [
			'收盘价折线图(￥).svg','收盘价对数变换折线图(￥).svg',
			'收盘价月日平均值(￥).svg','收盘价周日平均值(￥).svg',
			'收盘价星期均值(￥).svg'
	]:
		html_str = '	<object type="image/svg+xml" data="{0}"' 
		html_str += ' height=500></object>\n'
		html_file.write(html_str.format(svg))
	html_file.write('</body><html>')

	
