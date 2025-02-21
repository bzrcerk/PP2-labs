import re

text = r'Apple HelloWorld RegexPractice UPPERCASE lowercase Test123'

pattern = r'[A-Z][a-z]+'

res = re.findall(pattern, text)

print(res)