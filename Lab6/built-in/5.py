a = (True, True, True, 1, 2>1, 5>10)
b = (True, True, True, 1, 2>1, 5<10)

print("Yes") if all(a) else print("No")
print("Yes") if all(b) else print("No")