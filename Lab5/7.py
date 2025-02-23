import re

text = r'hello_world convert_this_example snake_case_string this_is_a_test'

pattern = r'\w*_\w*'

def repl(match):
	word = str(match.group(0))
	res = ''
	for i in range(len(word)):
		if word[i] == '_':
			res += word[i+1].upper()
		else:
			if i == 0 or word[i-1] != '_':
				res+=word[i]
	return res


res = re.sub(pattern, repl, text)

print(res)
		
