# coding=gbk
"""һ�������ڱ�ʾ��������"""
class Car():
	"""һ��ģ�������ļ򵥳���"""
	def __init__(self,make,model,year):
		"""��ʼ����������������"""
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0
	def get_descriptive_name(self):
		"""�������������������"""
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()
	def read_odometer(self):
		"""��ӡһ����Ϣ��ָ�����������"""
		print("This car has " + str(self.odometer_reading) + " miles on it.")
	def update_odometer(self,mileage):
		"""
		����̱��������Ϊָ����ֵ
		�ܾ�����̱����ز�
		"""
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer!")
	def increasement_odometer(self,miles):
		"""����̱��������ָ������"""
		self.odometer_reading += miles
