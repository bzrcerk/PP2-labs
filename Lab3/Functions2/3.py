from modules.module import movies

def take_cat(cat):
	res = []
	for i in movies:
		if i['category'] == cat:
			res.append(i['name'])
	print(res)
	
categ = str(input("Enter category that you want to see: \n"))

take_cat(categ)