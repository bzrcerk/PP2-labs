def rev(n):
	for i in range(n, 0, -1):
		yield i

n = int(input("Enter number: "))

a = rev(n)

for i in a:
	print(i, end=' ')