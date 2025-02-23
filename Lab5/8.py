import re

text = r'HelloWorldExample ThisIsATest RegexPracticeTask'

pattern = r'[A-Z][a-z]*'

res = re.findall(pattern, text)

print(res)