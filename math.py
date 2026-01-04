def __getpowertwo__(num):
    i = 2
    x = 1
    while i <= num:
        x += 1
        i *= i
    return x



print(__getpowertwo__(64))