import itertools

def perms(str):
	per = itertools.permutations(str)
	for i in per:
		print("".join(i))

str = str(input())

perms(str)
