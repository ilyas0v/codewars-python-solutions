import re
def generate_bc(url, separator):
    s=""
    url=url.replace("//","")
    url = url.replace("///","")
    lazimsiz = ["the","of","in","from","by","with","and", "or", "for", "to", "at", "a"]
    url_parts = url.split("/")
    if len(url_parts)==3:
        s='<a href="/">HOME</a>'
        s=s+separator
        if "index" in url_parts[2]:
            s=s+'<span class="active">'+url_parts[1].upper()+'</span>'
        elif "-" not in url_parts[1]:
            s=s+ '<a href="/'+url_parts[1]+'/">'+url_parts[1].upper()+'</a>'
            s=s+separator
            if "?" in url_parts[2]:
                son = url_parts[2].split("?")
                s=s+'<span class="active">'+son[0].upper()+'</span>'
            elif "." in url_parts[2]:
                son=url_parts[2].split(".")
                s=s+'<span class="active">'+son[0].upper()+'</span>'
            elif "-" in url_parts[2]:
                SON_HISSE = ""
                SON = url_parts[2].split("-")
                for S in SON:
                    SON_HISSE = SON_HISSE + S +" "
                SON_HISSE =SON_HISSE[:len(SON_HISSE)-1]
                s=s+'<span class="active">'+SON_HISSE.upper()+'</span>'
            else:
                s=s+'<span class="active">'+url_parts[2].upper()+'</span>'
        elif "-" in url_parts[1]:
            bash_herfler=""
            KK=url_parts[1].split("-")
            for k in KK:
                if k not in lazimsiz:
                    bash_herfler = bash_herfler+k[0]
    
            s=s+ '<a href="/'+url_parts[1]+'/">'+bash_herfler.upper()+'</a>'
            s=s+separator
            if "?" in url_parts[2]:
                son = url_parts[2].split("?")
                s=s+'<span class="active">'+son[0].upper()+'</span>'
            elif "." in url_parts[2]:
                son=url_parts[2].split(".")
                s=s+'<span class="active">'+son[0].upper()+'</span>'
            elif "-" in url_parts[2]:
                SON_HISSE = ""
                SON = url_parts[2].split("-")
                for S in SON:
                    SON_HISSE = SON_HISSE + S +" "
                SON_HISSE =SON_HISSE[:len(SON_HISSE)-1]
                s=s+'<span class="active">'+SON_HISSE.upper()+'</span>'
            else:
                s=s+'<span class="active">'+url_parts[2].upper()+'</span>'
    return s