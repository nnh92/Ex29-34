try:
    a, b = map(int, input('Nhap 2 so a, b: ').split())
    if a >= b:
        print('So thu nhat lon hon so thu hai!')
    else:
        i = a
        number = 0
        lst = list()
        while i <= b:
            if i % 5 == 0:
                if number <= 10:
                    number += 1
                    lst.append(i)
            i += 1

except:
    print('Dinh dang dau vao khong hop le!')

print(lst)
