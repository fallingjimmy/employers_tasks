import requests
import datetime
from xml.etree import ElementTree

class CurrencyAnalizer:
	def __init__(self, day_numbers=90):
		# self.d = str()
		# self.m = str()
		# self.y = str()
		self.url = 'http://www.cbr.ru/scripts/XML_daily_eng.asp'
		#self.params = {'date_req': f'{self.d}/{self.m}/{self.y}'}
		self.day_numbers = day_numbers
		self.date_values = {}

	def data_structure(self):
		date = datetime.date.today()
		for i in range(self.day_numbers):
			self.date_values[date] = {}
			y = str(date.year)
			m = str(date.month)
			d = str(date.day)
			if len(m) < 2:
				m = '0' + m
			if len(d) < 2:
				d = '0' + d
			params = {'date_req': f'{d}/{m}/{y}'}
			res = requests.get(self.url, params=params)
			root = ElementTree.fromstring(res.text)
			for child in root:
				self.date_values[date][child[3].text] = float(child[4].text.replace(",", "."))
			date = date - datetime.timedelta(1)
		return self.date_values


	def find_minimum(self):
		pass

	def find_maximum(self):
		pass

	def find_average(self):
		pass


test_object = CurrencyAnalizer()
print(test_object.data_structure())