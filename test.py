import currency_task

test_object = currency_task.CurrencyAnalizer(day_numbers=2)

def find_minimum():
	min = float('inf')
	min_dict = {}
	data_dict = test_object.data_structure()
	for date in data_dict.keys():
		for currency_name in data_dict[date].keys():
			if currency_name in min_dict:
				if data_dict[date][currency_name] < min_dict[currency_name]:
					min_dict[currency_name] = data_dict[date][currency_name]
			else:
				min_dict[currency_name] = data_dict[date][currency_name]
	return min_dict

def find_maximum():
	max = 0
	max_dict = {}
	data_dict = test_object.data_structure()
	for date in data_dict.keys():
		for currency_name in data_dict[date].keys():
			if currency_name in max_dict:
				if data_dict[date][currency_name] > max_dict[currency_name]:
					max_dict[currency_name] = data_dict[date][currency_name]
			else:
				max_dict[currency_name] = data_dict[date][currency_name]
	return max_dict

def find_average():
	average_dict = {}
	data_dict = test_object.data_structure()
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
	return average_dict

print(find_average())

