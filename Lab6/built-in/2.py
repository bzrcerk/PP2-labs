a = str(input("Enter a string: "))

ups = sum(map(lambda x: x.isupper(), a))
lws = sum(map(lambda x: x.islower(), a))

print(f'Uppercase: {ups} \nLowercase: {lws}')