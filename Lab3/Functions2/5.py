from modules.module import movies

def imdb_by_cat(cat):

	overall_imdb = 0
	cnt = 0

	for i in movies:
		if i['category'] == cat:
			overall_imdb += i['imdb']
			cnt += 1
	
	avg_imdb = overall_imdb / cnt

	print(round(avg_imdb, 1))

cat = str(input("Enter category and you will get an average IMDB through this category: \n"))

imdb_by_cat(cat)


