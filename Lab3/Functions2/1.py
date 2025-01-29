from modules.module import movies

def imdb_check(name):
	for i in movies:
		if i['name'] == name and i['imdb'] > 5.5:
			return True
	return False

mov_name = str(input("Enter movie name and you will take in return if its IMDB higher than 5.5: "))

print(imdb_check(mov_name))