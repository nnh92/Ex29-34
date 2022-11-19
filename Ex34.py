try:
    x = float(input("Nhap x: "))
    ni = int(input("Nhap n: "))

    if ni < 0:
        print('Vui long nhap n la so tu nhien!')
    else:
        n = 2*ni
        giaithua = 1
        S = 1 - x
        for i in range(2,n+1):
            giaithua *= i
            S += (-x**i)/giaithua
            #print(giaithua)
        print('Giai thua can tinh: ',S)

except:
    print('Dinh dang dau vao khong hop le!')