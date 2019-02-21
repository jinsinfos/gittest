import re
str="Where What When Why Who Whose"
x=re.compile("W")
str1=x.sub("--",str)
print(str1)