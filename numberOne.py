def sockMerchant(ar):
    temp = {}
    hasil = 0

    for angka in ar:
        if angka not in temp:
            temp[angka] = 1
        else:
            temp[angka] = temp[angka] + 1

    for total in temp:
        hasil = hasil + temp[total] // 2
    return hasil

n = 9
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
result = sockMerchant(ar)
print(result)