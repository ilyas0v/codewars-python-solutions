def solution(string,markers):
    ORIGINAL_STRING = string
    for m in markers:
        string = string.replace(m,"#")
    mas = string.split("#")
    SAXLANILACAQ = mas[0].strip()
    for hedd in mas:
        if "\n" in hedd:
            muveq = hedd.split("\n")
            for i in range(1,len(muveq)):
                SAXLANILACAQ = SAXLANILACAQ + "\n"+muveq[i].strip()
    return SAXLANILACAQ