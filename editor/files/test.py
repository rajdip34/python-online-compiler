import json

dates = ['2012-01-21', '2012-01-22', '2012-01-23']
prices = [635, 432, 90]

labels = [
	{
		"title":"First",
		"value": "10%"
	},{
		"title":"Second",
		"value": "31%"
	},{
		"title":"Third",
		"value": "125%"
	},
]

new = []

for i in range(0,len(dates)):
	new.append({
		"price": prices[i],
		"date": dates[i]
	})
	
print(json.dumps({
    "values": new,
    "labels": labels
}))






























































