def find_discounted(prices):
    qiym=prices.split(" ")
    indexx = []
    MASSIV=[]
    for i in range(0,len(qiym)):
        if i not in indexx:
            for j in range(i+1,len(qiym)):
                temp=str(int(qiym[j])-int(qiym[j])*0.25)
                T=temp.split(".")
                if qiym[i]==T[0] and j not in indexx:
                    MASSIV.append(qiym[i])
                    indexx.append(j)
                    indexx.append(i)
                    break
    s=""
    for M in MASSIV:
        s=s+M+" "
    return s[:len(s)-1]