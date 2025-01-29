def un(list):
	res = []
	for i in list:
		if i not in res:
			res.append(i)

	print(res)

x = list(input("Enter your list: "))

un(x)