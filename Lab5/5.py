import re

text = r'axb a123b ab aXyzZb acdb bbba abc'

pattern = r'a+\w*b\b'

res = re.findall(pattern, text)

print(res)