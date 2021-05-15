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
				self.date_values[str(date)] = {}
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
					self.date_values[str(date)][child[3].text] = float(child[4].text.replace(",", "."))
				date = date - datetime.timedelta(1)
			return self.date_values
		data_structure(self)


	def find_minimum(self):
		min = float('inf')
		min_dict = {}
		data_dict = self.date_values
		date_minimum = {}
		for date in data_dict.keys():
			for currency_name in data_dict[date].keys():
				if currency_name in min_dict:
					if data_dict[date][currency_name] < min_dict[currency_name]:
						min_dict[currency_name] = data_dict[date][currency_name]
						date_minimum[currency_name] = date
				else:
					min_dict[currency_name] = data_dict[date][currency_name]
					date_minimum[currency_name] = date
		for currency_name in min_dict.keys():
			print(f' Курс {currency_name} был минимальным {date_minimum[currency_name]} числа и составлял {min_dict[currency_name]} рублей')

	def find_maximum(self):
		max = 0
		max_dict = {}
		date_maximum = {}
		data_dict = self.date_values
		for date in data_dict.keys():
			for currency_name in data_dict[date].keys():
				if currency_name in max_dict:
					if data_dict[date][currency_name] > max_dict[currency_name]:
						max_dict[currency_name] = data_dict[date][currency_name]
						date_maximum[currency_name] = date
				else:
					max_dict[currency_name] = data_dict[date][currency_name]
					date_maximum[currency_name] = date
		for currency_name in max_dict.keys():
			print(f' Курс {currency_name} достигал максимум {date_maximum[currency_name]} числа и составлял {max_dict[currency_name]} рублей')

	def find_average(self):
		average_dict = {}
		data_dict = self.date_values
		count = 0
		for date in data_dict.keys():
			count += 1
			for currency_name in data_dict[date].keys():
				if currency_name in average_dict:
					average_dict[currency_name] += data_dict[date][currency_name]
				else:
					average_dict[currency_name] = data_dict[date][currency_name]
		for key in average_dict.keys():
			average_dict[key] /= count
		for currency_name in average_dict.keys():
			print(f'Средний курс {currency_name} за {self.day_numbers} дней составляет {average_dict[currency_name]}')
		


test_object = CurrencyAnalizer(day_numbers=3)
test_object.find_minimum()
test_object.find_maximum()
test_object.find_average()