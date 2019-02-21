def MyNum():
    num=0
    yield num

    num=num+1
    yield num

    num=num+1
    yield num

    num=num+1
    yield num

for i in MyNum():
    print(i)