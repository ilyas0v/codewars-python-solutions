def pattern(n):
    s=""
    k=n
    for I in range(0,n):
        for i in range(I,0,-1):
            s=s+str(k)[len(str(k))-1]
            k=k-1
        for j in range(n-I,0,-1):
            s=s+str(n-I)[len(str(n-I))-1]
        s=s+"\n"
        k=n
            
    return s[:len(s)-1]