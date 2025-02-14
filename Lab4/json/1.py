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

print(f"{'DN'.ljust(dn_width)}{'Description'.ljust(des_width)}{'Speed'.ljust(speed_width)}{'MTU'.ljust(mtu_width)}")
print(f"{'-'*(dn_width-1)} {'-'*(des_width-1)} {'-'*(speed_width-1)} {'-'*(mtu_width-1)}")


for src in source:
	data_res = src["l1PhysIf"]["attributes"]
	dn = data_res["dn"].ljust(dn_width)
	des = data_res['descr'].ljust(des_width)
	speed = data_res['speed'].ljust(speed_width)
	mtu = data_res['mtu'].ljust(mtu_width)
	print(dn, des, speed, mtu)