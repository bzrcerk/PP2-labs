inp = 'test.txt'
out = 'output.txt'

data = []

with open(inp, 'r') as file:
	data = file.readlines()

with open(out, 'w') as file:
	for i in data:
		file.writelines(i)