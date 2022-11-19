n = int(input('Nhap so n: '))

time = n +1
for i in range(n):
    lst = []
    for j in range(1,time):
        lst.append(j)
    print(str(lst).replace(',',' '))
    time -= 1