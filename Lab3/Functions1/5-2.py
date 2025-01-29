def perm(a,size):
	if size == 0:
		res = ''.join(a)
		print(res)
		return
	

	for i in range(size):
		perm(a, size-1)
		if size % 2 != 0:
			a[0], a[size-1] = a[size-1], a[0]
		else:
			a[i], a[size-1] = a[size-1], a[i]

str = list(input("Enter your str: "))

perm(str, len(str))