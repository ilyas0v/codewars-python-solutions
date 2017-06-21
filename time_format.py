import math
def format_duration(seconds):
    year = math.floor(seconds/31536000)
    seconds =seconds - year*31536000
    day = math.floor(seconds/86400)
    seconds = seconds-day*86400
    hour = math.floor(seconds/3600)
    seconds = seconds - hour*3600
    minute = math.floor(seconds/60)
    seconds-=minute*60
    s=""
    if year>0:
        yearsss = str(year).split(".")
        year = yearsss[0]
        year = int(year)
        if year>1:
           s+=str(year)+" years, "
        else:
            s+=str(year)+" year, "

    if day>0:
        daysss = str(day).split(".")
        day = daysss[0]
        day = int(day)
        if day>1:
           s+=str(day)+" days, "
        else:
            s+=str(day)+" day, "

    if hour>0:
        hoursss = str(hour).split(".")
        hour = hoursss[0]
        hour = int(hour)
        if hour>1:
           s+=str(hour)+" hours, "
        else:
            s+=str(hour)+" hour, "

    if minute>0:
        minutesss = str(minute).split(".")
        minute = minutesss[0]
        minute = int(minute)
        if minute>1:
           s+=str(minute)+" minutes, "
        else:
            s+=str(minute)+" minute, "

    if seconds>0:
        secondsss = str(seconds).split(".")
        seconds = secondsss[0]
        seconds= int(seconds)
        if seconds>1:
           s+=str(seconds)+" seconds, "
        else:
            s+=str(seconds)+" second, "
    s=s[:len(s)-2]
    son_vergul = s.rfind(",")
    if son_vergul>0:
        s=s[:son_vergul]+" and"+s[son_vergul+1:]
    if s=="":
        return 'now'
    return s