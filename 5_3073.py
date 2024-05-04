for n in range(100,1000):
    c1 = int (str(n)[0])
    c2 = int(str(n)[1])
    c3 = int(str(n)[2])
    a = sorted ([c1,c2,c3])
    dmax = int(str(a[2])+str(a[1]))
    dmin = int(str(a[0])+str(a[1]))
    r = dmax - dmin
    if r ==5:
        print(n,r)
    
               
    
    
