def pattern(n):
    s=""
    k=1
    for i in range(0,n):
        s=s+(n-i-1)*" "
        while k<=i+1:
            s=s+str(k)[len(str(k))-1]
            k=k+1
        k=k-1
        while k>1:
            s=s+str(k-1)[len(str(k-1))-1]
            k=k-1
        s=s+(n-i-1)*" "
        s=s+"\n"
        k=1
    return s[:len(s)-1]