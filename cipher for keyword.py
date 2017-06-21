def keyword_cipher(msg, keyword):
    s = ""
    msg = msg.lower()
    alfa = "abcdefghijklmnopqrstuvwxyz"
    D = {}
    result=""
    for k in keyword:
        if k not in s:
            s=s+k
    for a in alfa:
        if a not in s:
            s=s+a
    for i in range(0,26):
        D[alfa[i]] = s[i]
    for m in msg:
        if m!=" ":
            result+=D[m]
        else:
            result+=" "
    return result
    