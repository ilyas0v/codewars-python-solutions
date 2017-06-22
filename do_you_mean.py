import operator

def find_most_similar(words,term):
    if term in words:
        return term
    k=0
    D={}
    for word in words:
        D[word]=0    
    for word in words:
        if len(word)!=len(term):
            D[word]+=0.5*abs(len(word)-len(term))
        k=0
        for i in range(0,len(word)-1):
            if word[i:k+2] in term:
                D[word]-=1
            k+=1
        
    D = sorted(D.items(), key=operator.itemgetter(1))
    for d in D:
        return "Do you mean : "+ d[0]
