j=0
i=1
print(f"{j},{i}",end=',')
while True:
    c=i+j
    print(c, end=",")
    j=i
    i=c
    
