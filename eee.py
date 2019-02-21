import re

str="my phone number is 9645313924 and my brothers number is 9048712671"

#result=re.findall(r"\d+",str)
#result=re.findall(r"\d{10}",str)
result=re.findall(r"\d\d\d\d\d\d\d\d\d\d",str)
print (result)