import re
str="what is your name? how old are you? see you later"
result=re.findall(r"[\s\w]",str)
print(result)