def pal(str):
	if str == str[::-1]:
		return True
	return False

x = str(input())

print(pal(x))