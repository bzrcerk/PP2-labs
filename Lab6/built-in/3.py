is_pal = lambda s: s.lower() == s.lower()[::-1]

a = str(input("Enter a string: "))

print("Yes") if is_pal(a) else print("No")