def strip_url_params(url, params_to_strip = []):
    um = url.split("&")
    umm = um[0].split("?")
    mas = []
    if len(umm)==2:
        mas.append(umm[1])
    else:
        return umm[0]
    for i in range(1,len(um)):
        mas.append(um[i])
    mas2 = []
    muveqqetiler = []
    for m in mas:
        muveq = m.split("=")
        if muveq[0] not in muveqqetiler:
            if muveq[0] not in params_to_strip:
                mas2.append(m)
                muveqqetiler.append(muveq[0])
    s = umm[0]+"?" + mas2[0]+"&"
    for i in range(1,len(mas2)):
        s+=mas2[i]+"&"
    return s[:len(s)-1]