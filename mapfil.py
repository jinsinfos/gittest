list=[1,2,3,4,5,6,7,8,9,10]
mapfil=filter( lambda x:x%2==0,map(lambda x:x*x,list))
print(mapfil)
for i in mapfil:
    print(i)

