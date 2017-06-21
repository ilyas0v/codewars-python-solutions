def duzelish_et(str):
    if len(str)>30:
    	lazimsiz = ["the","of","in","from","by","with","and", "or", "for", "to", "at", "a"]
    	hisse = []
    	yekun = ""
    	if "-" in str:
    		hisse = str.split("-")
    		for h in hisse:
    			if h not in lazimsiz:
    				yekun+=h[0]
    	return yekun
    elif "-" in str:
        STR=""
        mas=str.split("-")
        for m in mas:
            STR=STR+m+" "
        return STR[:len(STR)-1]
    return str
def generate_bc(url,sep):
    s=""
    url=url.replace("//","")
    url_parts=url.split("/")
    if len(url_parts)==1:
        return '<span class="active">HOME</span>'
    elif len(url_parts)==2:
        if "index" in url_parts[1]:
            return '<span class="active">HOME</span>'
        elif url_parts[1]!="":
            return '<a href="/">HOME</a>'+sep+'<span class="active">'+sonuncunu_duzelish(url_parts[1]).upper()+'</span>'
        else:
            return '<span class="active">HOME</span>'
    s+='<a href="/">HOME</a>'
    s+=sep
    yazilacaq="/"
    for i in range(1,len(url_parts)-2):
        yazilacaq+=url_parts[i]+"/"
        s+='<a href="'+yazilacaq+'">'+duzelish_et(url_parts[i]).upper()+'</a>'
        s+=sep
    if "index" in url_parts[len(url_parts)-1]:
        s=s+'<span class="active">'+sonuncunu_duzelish(url_parts[len(url_parts)-2]).upper()+'</span>'
    else:
        yazilacaq+=url_parts[len(url_parts)-2] +"/"
        s+='<a href="'+yazilacaq+'">'+duzelish_et(url_parts[len(url_parts)-2]).upper()+'</a>'
        s+=sep
        s=s+'<span class="active">'+sonuncunu_duzelish(url_parts[len(url_parts)-1]).upper()+'</span>'
    return s

def sonuncunu_duzelish(str):
    if ".html" in str or ".asp" in str or ".php" in str or ".htm" in str:
        M=str.split(".")
        str = M[0]
    if "#" in str:
        M=str.split("#")
        str=M[0]
    if "?" in str:
        M=str.split("?")
        str= M[0]
    if "-" in str:
        if len(str)>30:
            duzelish_et(str)
        else:
            M=str.split("-")
            KK=""
            for MM in M:
                KK=KK+MM+" "
            return KK[:len(KK)-1]
    return duzelish_et(str)