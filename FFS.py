x = "chi"  # thông tin cần mã hóa

#chuyển từ dạng chữ sang dạng thập phân
def deg(x):
    X = 0
    for i in range(0, len(x)):
        X = X + (ord(x[2 - i]) - 97) * pow(26, i)
    return X

def FFS(p, q, id, s, b, r, e):
    n = p * q
    X = deg(id)
    v = [0, 0, 0]
    for i in range(3):
        v[i] = (pow(-1, b[i], n) * pow(s[i], -2, n)) % n
    print('A đăng ký khóa công khai v1, v2, v3 và n: ', v, ' ', n)
    x = (pow(-1, b[1], n) * pow(r, 2, n)) % n
    print('A gửi cho B x: ', x)
    print('B gửi cho A vector e: ', e)
    y = r
    for i in range(3):
        y = (y * pow(s[i], e[i], n)) % n
    print('A gửi câu trả lời y cho B: ', y)
    z = pow(y, 2, n)
    for i in range(3):
        z = (z * pow(v[i], e[i], n)) % n
    print('B tính z: ', z)
    if z == x or z == pow(-x, 1, n):
        print("true")

p = 487
q = 491
n = p * q
b = [1, 0, 0]
s = [492, 493, 494]
k = 3
t = 1
r = 495
e = [0, 1, 0]
FFS(p, q, 'chi', s, b, r, e)
