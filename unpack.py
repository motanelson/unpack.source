import os
import struct
print( "\033c\033[40;37m\n ? ")
a="my.dat"
b=[]
num=[1,256,256*256,256*256*256]
f1=open(a,"rb")
while(1):
    try:
        rr=0
        r=f1.read(4)
        if len(r)<4:
            break
        counter=0
        for n in r:
            n:int=n
            rr:int=rr+n*num[counter]
            counter=counter+1
        b=b+[rr]
    except:
        break
f1.close()
print(b)