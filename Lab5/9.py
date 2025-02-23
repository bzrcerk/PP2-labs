import re

text = r'HelloWorldExample ThisIsATest RegexPracticeTask'

pattern = r'[A-Z][a-z]*'

res = re.findall(pattern, text)

res_f = ' '.join(res)

print(res_f)