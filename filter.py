list=[1,2,3,4,5,6,7,8,9,10]
fil=filter(lambda x: x%2==0,list)
print(fil)
for i in fil:
    print(i)