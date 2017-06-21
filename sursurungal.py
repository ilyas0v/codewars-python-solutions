def sursurungal(txt):
    M = txt.split(" ")
    if len(M)==2:
        quan = int(M[0])
        if quan<2:
            return txt
        else:
            if quan==2:
                return M[0]+" "+"bu"+M[1][:len(M[1])-1]
            elif quan>=3 and quan<=9:
                return M[0]+" "+M[1][:len(M[1])-1]+"zo"
            elif quan>9:
                return M[0]+" "+"ga"+M[1][:len(M[1])-1]+"ga"
    else:
        S=""
        k=0
        indeks=0
        for m in M:
            if k==1:
                if int(M[indeks-1])<2:
                    S=S+m+" "
                    k=0
                elif int(M[indeks-1])==2:
                    S=S+"bu"+m[:len(m)-1]+" "
                    k=0
                elif int(M[indeks-1])>=3 and int(M[indeks-1])<=9:
                    S=S+m[:len(m)-1]+"zo"+" "
                    k=0
                else:
                    S=S+"ga"+m[:len(m)-1]+"ga"+" "
                    k=0
            else:
                if m[0].isdigit():
                    k=1
                    S=S+m+" "
                else:
                    S=S+m+" "
            indeks+=1
        return S[:len(S)-1]