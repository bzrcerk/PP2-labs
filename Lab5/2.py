import re

text = r'a ab abb abbb aBBBB acb bba aaabb'

pattern = 'a+[Bb]{2,3}'

res = re.findall(pattern, text)

print(res)