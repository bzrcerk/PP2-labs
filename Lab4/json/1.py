import json

with open('./data/data.json', 'r') as file:
	data = json.load(file)

source = data.get('imdata')


headers = {"DN" : 50, "Description" : 20, "Speed" : 10, "MTU" : 10}

dn_width = 50
des_width = 20
speed_width = 10
mtu_width = 10

print("Interface Status")
print("="*(sum(headers.values())))

for head in headers:
	print(head.ljust(headers[head]-1), end=' ')
print()
for sep in headers:
	print('-'*(headers[sep]-1), end=' ')
print()



for src in source:
	data_res = src["l1PhysIf"]["attributes"]
	dn = data_res["dn"].ljust(headers['DN'])
	des = data_res['descr'].ljust(headers['Description']-2)
	speed = data_res['speed'].ljust(headers['Speed'])
	mtu = data_res['mtu'].ljust(headers['MTU'])
	print(dn, des, speed, mtu)