#ska skriva om siffror till tal


s = "III"
s = "LVIII"
s = "DCXXI"
s = "MMCCCXCIX"
s = "MCMXCIV"


# I=1
# V=5
# X=10
# L=50
# C=100
# D=500
# M=1000


b = 0
siffra = 0
for i in s[::-1]:
    if i == "M":
        b += 1000
        if siffra > 1000:
            siffra = 1000
            b -= 2000
        else:
            siffra = 1000
    elif i == "D":
        b += 500
        if siffra > 500:
            siffra = 500
            b -= 400
        else:
            siffra = 500
    
    elif i == "C":
        b += 100
        if siffra > 100:
            siffra = 100
            b -= 200
        else:
            siffra = 100


    elif i == "L":
        b += 50
        if siffra > 51:
            b -= 100
            siffa = 50
        else:
            siffra = 50

    elif i == "X":
        b += 10
        if siffra > 11:
            siffra = 10
            b -= 20
        else:
            siffra = 10

    elif i == "V":
        b += 5
        if siffra > 6:
            siffra = 5
            b -= 10
        else:
            siffra = 5

    elif i == "I":
        b += 1
        if siffra > 2:
            siffra = 1
            b -= 2      

    print(b)



#uppdaterad version med hjälp och kolla upp


s = "MCMXCIV"

translation = {
    "I":1,
    "V":5,
    "X":10,
    "L":50,
    "C":100,
    "D":500,
    "M":1000,
}


summan = 0
pre_num = 0
for i in s[::-1]:
    värdet = translation[i]
    
    if värdet >= pre_num:
        summan += värdet    
    else:
        print("minus")
        summan -= värdet
        
    pre_num = värdet
    print("summa",summan)
