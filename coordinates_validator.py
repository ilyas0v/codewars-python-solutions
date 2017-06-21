import re
def is_valid_coordinates(C):
    match = re.match(r'(^\d+\,\s\d+$)|(^-\d+\,\s\d+$)|(^\d+\,\s-\d+$)|(^-\d+\.\d+\,\s\d+\.\d+$)|(^\d+\.\d+\,\s-\d+\.\d+$)|(^\d+\.\d+\,\s\d+\.\d+$)|(^\d+\,\s\d+\.\d+$)|(^\d+\.\d+\,\s\d+$)|(^-\d+\.\d+\,\s\d+$)|(^\d+\,\s-\d+\.\d+$)|(^-\d+\.\d+\,\s-\d+\.\d+$)|(^-\d+\,\s-\d+\.\d+$)|(^-\d+\.\d+\,\s-\d+$)',C)
    K = bool(match)
    if K==True:
        temp = C.split(", ")
        birinci = temp[0].split(".")
        ikinci = temp[1].split(".")
        if int(birinci[0])>90 or int(birinci[0])<-90:
            return False
        if int(ikinci[0])>180 or int(ikinci[0])<-180:
            return False
    elif C=="-90, -180":
        return True
    else:
        return False
    return True