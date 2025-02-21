x = 1
power = 3 % 7

mass = [1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1]

for i in mass[::-1]:
	if i == 1: x = (x * power) % 7
	power = (power * power) % 7
	print(f'x = {x} pow = {power}')

print(x)