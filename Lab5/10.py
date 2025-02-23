import re

text = r'HelloWorldExample ThisIsATest RegexPracticeTask'

pattern = r'[A-Z][a-z]*([A-Z][a-z]*)*'

def repl(match):
	sent = str(match.group(0))
	res = sent[0].lower()

	for i in range(1, len(sent)):
		if sent[i].isupper():
			res += '_' + sent[i].lower()
		else:
			res += sent[i]

	return res

res = re.sub(pattern, repl, text)


print(res)
