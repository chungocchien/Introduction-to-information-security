pp = 39051 * pow(2, 6001) - 1  #số nguyên tố sophie germain có 1812 chữ số
p = 2*pp + 1
# tìm phần tử nguyên thủy của p
def element(p):
    for i in range(2, p):
        if pow(i, (p - 1) // 2, p) != 1 and pow(i, (p - 1) // pp, p) != 1:
            return i
    return -1


alpha = element(p)
a = 31231231
beta = pow(alpha, a, p)

x = 20020004#thông tin cần mã hóa
k = 1000

#mã hóa
y1 = pow(alpha, k, p)
y2 = (pow(beta, k, p) * x) % p
print('y1:', y1)
print('y2:', y2)

#giải mã
xx = (y2 * pow(y1, p - a - 1, p)) % p
print(xx)
