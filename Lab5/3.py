import re

text = r"hello_world regex_practice test_case Python_Regex valid_variable not_valid123 _underscore"

pattern = r'_\w*'

res = re.findall(pattern, text)

print(res)