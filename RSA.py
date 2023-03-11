pp = 713851138 * pow(10, 1854) + 1  # 1863 chữ số
qq = 39051 * pow(2, 6001) - 1  # 1812 chữ số
p = 2 * pp + 1
q = 2 * qq + 1
e = 5


# euclid mở rộng
def ext_euclid(a, b):
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


d = ext_euclid(2 * pp * 2 * qq, e)
if d < 0:
    d += 4 * pp * qq
x = int(input())#số cần mã hóa
y = pow(x, e, p * q)#bản mã
print(y)
