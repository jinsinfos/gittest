def readfile(name):
    try:
        f=open(name,'r',encoding='utf-8')
        return f.readlines()
    except:
        print("exception occured::")
    finally:
        pass
def process(lines):
    m=[]
    for x in lines:
        data=x.split(",")
        sum=int(data[2])+int(data[3])+int(data[4])+int(data[5])
        m.append((data[0],data[1],sum))
    return m
def main():
   filename="students.csv"
   lines=readfile(filename)
   s=process(lines)
   print(s)
main()
