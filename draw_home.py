def my_crib(n):
    ev=""
    k=n
    for i in range(0,n):
        ev=ev+(k)*" "+"/"+i*2*" "+"\\"+(k)*" "+"\n"
        k-=1
    #for i in range(0,n):
    ev=ev+"/"+2*n*"_"+"\\\n"
    for i in range(0,n-1):
        ev=ev+"|"+2*n*" "+"|"+"\n"
    ev=ev+"|"+2*n*"_"+"|"
    return ev
while True:
	inp = input("Nece mertebeli? :  ")
	print(my_crib(int(inp)))