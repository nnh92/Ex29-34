n = int(input('Nhap so n: '))

time = 1
for i in range(n):
    lst = []
    time += 1
    for j in range(1,time):
        lst.append(j)
    print(str(lst).replace(',',' '))