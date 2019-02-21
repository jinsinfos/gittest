import re
str="ssssssssssss what is your name? jhfjcdhjdhefc where is his house? ggggggggggggg when will he come here?"
result=re.findall(r"(((what|where|when|how)([\s\w])+) ([\?])",str)
print(result)