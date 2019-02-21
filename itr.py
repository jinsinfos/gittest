def MyRange(start,stop):
    while start<stop:
        start=start+1
        yield start
itr = iter(MyRange(10,20))

for i in itr:
    print (i)
