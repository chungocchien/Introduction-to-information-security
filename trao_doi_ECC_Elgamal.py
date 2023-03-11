p = 1055501
a = 0
b = 4

(xP,yP) = (24749,8957)


# y^2 = x^3 + ax + b
def ext_euclid(a, b):
    b = b % a
    x1 = 0
    x2 = 1
    y1 = 1
    y2 = 0
    while b != 0:
        k = a // b
        r = a % b
        x = x2 - k * x1
        y = y2 - k * y1
        a = b
        b = r
        x2 = x1
        x1 = x
        y2 = y1
        y1 = y
    return y2


# phép cộng
def add(x1, y1, x2, y2):
    lamda = 0
    if x1 == x2 and y1 == y2:
        c, d = (3 * x1 * x1 + a), (2 * y1)
    else:
        c, d = (y2 - y1), (x2 - x1)
    lamda = (c * ext_euclid(p, d)) % p
    x3 = (lamda * lamda - x1 - x2) % p
    y3 = (lamda * (x1 - x3) - y1) % p
    return (x3, y3)

#phép nhân
def multiple(n, x, y):
    xx, yy = x, y
    for i in range(n-1):
        xx, yy = add(xx, yy, x, y)
    return xx, yy

dA = 2063
dB = 3929
def ECC_El(xP, yP, dA, dB):
    print("A chọn số ngẫu nhiên dA: ", dA)
    (xBa,yBa) = multiple(dA, xP, yP)
    print("A gửi cho B số Ba: ", (xBa,yBa))
    print("B chọn số ngẫu nhiên dB: ", dB)
    (xBb,yBb) = multiple(dB, xP, yP)
    print("B gửi cho A số Bb: ", (xBb, yBb))
    (xKAB,yKAB) = multiple(dB,xBa,yBa)
    (xKBA,yKBA) = multiple(dA,xBb,yBb)
    if (xKAB,yKAB) == (xKBA,yKBA):
        print("khóa chung kAB: ",(xKAB, yKAB))

ECC_El(xP,yP,dA,dB)