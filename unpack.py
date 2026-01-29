def unpacks(r):
    try:
        rr=0
        counter=0
        for n in r:
            n:int=n
            rr:int=rr+n*num[counter]
            counter=counter+1
        
        return rr
    except:
        return 0

print( "\033c\033[40;37m\n ? ")
a="my.dat"
b=[]
num=[1,256,256*256,256*256*256]
f1=open(a,"rb")
while(1):
    try:
        
        r=f1.read(4)
        if len(r)<4:
            break
        rr=unpacks(r)
        b=b+[rr]
    except:
        break
f1.close()
print(b)