import re

text = r'a ab abb abbb aBBBB acb bba aaabb'

pattern = 'a+b*'

res = re.findall(pattern, text)

print(res)