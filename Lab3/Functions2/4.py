from modules.module import movies

def avg_imdb():
	overall_imdb = 0

	for i in movies:
		overall_imdb+=i['imdb']

	avg_i = overall_imdb/len(movies)
	print(round(avg_i, 1))

avg_imdb()