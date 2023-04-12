v1 = list(map(int, input().split()))
v2 = list(map(int, input().split()))
resultado = []
for i in range(len(v1)):
    total = v1[i] * v2[i]
    resultado.append(total)

r = 0
for i in resultado:
    r += i

print(r)

