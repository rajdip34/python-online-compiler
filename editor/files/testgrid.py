import json
from datetime import date, datetime, timedelta
import random

#dates = [date(2010,1,1),date(2010,1,2),date(2010,1,3)]

def make_prices(col1, col2):
	date = datetime(2003,8,1,12,4,5)
	dates = []
	prices=[]
	for i in range(100):
		date += timedelta(days=1)
		t = date.strftime('%m/%d/%Y')
		dates.append(t)
		prices.append(100.0*random.random())
	
	graph = []

	for i in range(0,len(dates)):
		graph.append({
			'date': dates[i],
			'price': prices[i]
		})
	
	return {
   	 "values": graph,
	}

def make_month_year():
	date = datetime(2003,8,1,12,4,5)
	month = []
	year=[]
	for i in range(100):
		date += timedelta(days=1)
		t = date.strftime('%m/%d/%Y')
		month.append(date.strftime('%F'))
		year.append(date.strftime('%Y'))
	
	graph = []

	for i in range(0,100):
		graph.append({
			'month': month[i],
			'year': year[i]
		})
	
	return {
   	 "values": graph,
	}

def make_age(name):
	alpha = [chr(i) for i in range(97, 123)]
	actor = []
	age =[]
	for i in range(100):
		actor.append("".join(random.sample(alpha, 7)))
		age.append(random.randint(10, 50))
	
	graph = []

	for i in range(0,len(actor)):
		graph.append({
			name: actor[i],
			'age': age[i]
		})
	
	return {
   	 "values": graph,
	}


dataset1 =  make_prices('dates','price')
dataset2 = make_month_year()
dataset3 = make_age('men')
dataset4 = make_age('women')

result = [dataset1, dataset2, dataset3, dataset4]
print(json.dumps(result))

	











