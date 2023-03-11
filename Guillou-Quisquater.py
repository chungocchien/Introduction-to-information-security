# chuyển từ dạng chữ sang dạng thập phân
def deg(x):
    X = 0
    for i in range(0, len(x)):
        X = X + (ord(x[2 - i]) - 97) * pow(26, i)
    return X


def GQ(u, p, q, b, id, s, k, r):
    n = p * q
    v = pow(pow(u, -1, n), b, n)
    ID = deg(id)
    print('A chuyển cho TA số v: ', v)
    print('TA cấp cho A hông tin C(A) gồm ID, v, s: ', ID, ', ', v, ', ', s)
    gama = pow(k, b, n)
    print('A gửi cho B C(A) và gama: ', gama)
    print('sau khi kiểm thử B gửi cho A số r: ', r)
    y = (k * pow(u, r, n)) % n
    print('A gửi cho B số y: ', y)
    gama2 = (pow(v, r, n) * pow(y, b, n)) % n
    print('B thử điều kiện')
    print(gama == gama2)


# do không nhớ số hôm trc nên em lấy bừa số
id = 'chi'
p = 191
q = 193
u = 199
b = 211
s = 103
k = 179
r = 181
GQ(u, p, q, b, id, s, k, r)
