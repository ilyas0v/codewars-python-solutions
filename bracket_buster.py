import re
def bracket_buster(string):
    DD="0123456789"
    #if "[[[[" in string:
     #   print(string)
    if isinstance(string, (str)):
        match = re.findall(r'\[[\w\s\"\'?\d-]+\]|\[\[+\]|\[\]',string)
        mas=[]
        for m in match:
            if len(m)==2:
                mas.append("")
            else:
                mas.append(m[1:len(m)-1])
        return mas
    return "Take a seat on the bench."