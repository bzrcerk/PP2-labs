from modules.module import movies

def list_of_highest(list):
	res = []
	for i in list:
		if i['imdb'] > 5.5:
			res.append(i['name'])
	return res

print(list_of_highest(movies))