n = int(input('Nhap so dong n = '))

k = 1
a = 0
for i in range(n):
    khoangtrang = ' '*((n - i)*2-1)
    print(khoangtrang, end = ' ')
    for j in range(1, k + 1):
        print(chr(65 + a), end = ' ')
        a += 1
    k += 2
    print()