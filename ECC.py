p = 1000003
a = 0
b = 4
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


# điểm P
xp, yp = (90514, 196)
xB, yB = xp, yp
s = 10
for i in range(s - 1):
    xB, yB = add(xB, yB, xp, yp)

# bản tin M
xM, yM = (557543, 147196)
k = 9
# M1
xM1, yM1 = xp, yp
for i in range(k - 1):
    xM1, yM1 = add(xM1, yM1, xp, yp)
# M2
xM2, yM2 = xM, yM
for i in range(k):
    xM2, yM2 = add(xM2, yM2, xB, yB)
print(xM1, yM1, xM2, yM2)

# giải mã bằng cách dò xem M1 và M2 bằng bao nhiêu lần P
xx, yy = xp, yp
l1 = 1
while (xx != xM1 or yy != yM1):
    xx, yy = add(xx, yy, xp, yp)
    l1 += 1
xx1, yy1 = xp, yp
l2 = 1

while (xx1 != xM2 or yy1 != yM2):
    xx1, yy1 = add(xx1, yy1, xp, yp)
    l2 += 1

l = (l2 - s * l1) % p
xMM, yMM = xp, yp
for i in range(l - 1):
    xMM, yMM = add(xMM, yMM, xp, yp)
print(xMM, yMM)  # thông tin sau khi được giải mã
print((xMM == xM and yMM == yM))
