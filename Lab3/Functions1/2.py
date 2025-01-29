def far_to_cel(temp_far):
	c = (5 / 9) * (temp_far - 32)
	print(round(c, 3))

temp = float(input("Enter temperature in Fahrenheit: "))

far_to_cel(temp)

