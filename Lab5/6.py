import re

text = r'Hello, world. How are you? This is a test, a simple one. Replace spaces, commas, and dots. Regex is fun.'

pattern = r'[ .,]'

res = re.sub(pattern, ':',text)

print(res)