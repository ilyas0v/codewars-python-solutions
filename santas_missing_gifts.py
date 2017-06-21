import math
def gifts(number):
    mas=[]
    GIFTS = {
        1: 'Toy Soldier',
        2: 'Wooden Train',
        4: 'Hoop',
        8: 'Chess Board',
        16: 'Horse',
        32: 'Teddy',
        64: 'Lego',
        128: 'Football',
        256: 'Doll',
        512: "Rubik's Cube"
    }
    ededler = [512,256,128,64,32,16,8,4,2,1]
    if number in GIFTS:
        mas.append(GIFTS[number])
    else:
        if number>=512:
            say=math.floor(number/512)
            number = number - say*512
            for i in range(0,say):
                mas.append(GIFTS[512])
        if number>=256:
            say=math.floor(number/256)
            number = number - say*256
            for i in range(0,say):
                mas.append(GIFTS[256])
        if number>=128:
            say=math.floor(number/128)
            number = number - say*128
            for i in range(0,say):
                mas.append(GIFTS[128])
        if number>=64:
            say=math.floor(number/64)
            number = number - say*64
            for i in range(0,say):
                mas.append(GIFTS[64])
        if number>=32:
            say=math.floor(number/32)
            number = number - say*32
            for i in range(0,say):
                mas.append(GIFTS[32])
        if number>=16:
            say=math.floor(number/16)
            number = number - say*16
            for i in range(0,say):
                mas.append(GIFTS[16])
        if number>=8:
            say=math.floor(number/8)
            number = number - say*8
            for i in range(0,say):
                mas.append(GIFTS[8])
        if number>=4:
            say=math.floor(number/4)
            number = number - say*4
            for i in range(0,say):
                mas.append(GIFTS[4])
        if number>=2:
            say=math.floor(number/2)
            number = number - say*2
            for i in range(0,say):
                mas.append(GIFTS[2])
        if number>=1:
            say=math.floor(number/1)
            number = number - say*1
            for i in range(0,say):
                mas.append(GIFTS[1])
    mas.sort()
    return mas