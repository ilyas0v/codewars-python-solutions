import re
def acronym_buster(message):
    ACR = {
    "KPI":"key performance indicators",
    "EOD":"the end of the day",
    "TBD":"to be decided",
    "WAH":"work at home",
    "IAM":"in a meeting",
    "OOO": "out of office",
    "NRN": "no reply necessary",
    "CTA":"call to action",
    "SWOT":"strengths, weaknesses, opportunities and threats"
    }
    S=""
    mesajlar=message.split(" ")
    for m in mesajlar:
        if m.isupper() and len(m)>=3 and m not in ACR and m[:len(m)-1] not in ACR and "." not in m:
            return m+' is an acronym. I do not like acronyms. Please remove them from your email.'
        elif "." in m and m[:len(m)-1] not in ACR and len(m)>3 and m.isupper():
            return m[:len(m)-1]+' is an acronym. I do not like acronyms. Please remove them from your email.'
        elif m in ACR:
            S=S+ACR[m]+" "
        elif m[:len(m)-1] in ACR:
            S=S+ACR[m[:len(m)-1]]+"."+" "
        else:
            S=S+m+" "
    S=S[:len(S)-1]
    boshluq_ve_bash = re.findall(r'\.\s\w',S)
    for b in boshluq_ve_bash:
        S=S.replace(b,". "+b[2].upper())
    S = S[0].upper() + S[1:]
    return S