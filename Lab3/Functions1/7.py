def has_33(ints):
	for i in range(len(ints)-1):
		if ints[i] == ints[i+1] and ints[i] == "3":
			return True
	return False


x = list(input())

print(has_33(x))

