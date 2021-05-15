impif len(m) < 2:
		m = '0' + m
	if len(d) < 2:
		d = '0' + dimport datetime
import requests
from bs4 import BeautifulSoup
from xml.etree import ElementTree

class CurrencyDate:
	def __init__(self, date):
		self.date = date
		self.currency_value_dict ={}


	def append_rate(self, currency, value):
		self.currency_value_dict[currency] = value

	def __repr__(self):
		return f'({self.date}, {self.currency_value_dict})'


def main():
	date = datetime.date.today()
	currency_exchange_rate = []
	currency_name = []

	for i in range(90):
		y = str(date.year)
		m = str(date.month)
		d = str(date.day)
		if len(m) < 2:
			m = '0' + m
		if len(d) < 2:
			d = '0' + d
		day_object = CurrencyDate(date)
		url = 'http://www.cbr.ru/scripts/XML_daily_eng.asp'
		params = {'date_req': f'{d}/{m}/{y}'}
		res = requests.get(url, params=params)
		root = ElementTree.fromstring(res.text)
		for child in root:
			day_object.append_rate(child[3].text, child[4].text)
		currency_exchange_rate.append(day_object)
		date = date - datetime.timedelta(1)
	return currency_exchange_rate

xml_list = main()
for i in xml_list:
	




			
			










