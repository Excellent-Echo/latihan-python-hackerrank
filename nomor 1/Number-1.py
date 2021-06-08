import sys

def sockMerchant(n, ar):
    # print("n", n)
    # print("ar", ar)
    temp = {}
    # print("array kosong", temp)
    hasil = 0
    # print("int kosong", hasil)

    for angka in ar:
        # print("angka", angka)
        if angka not in temp:
            temp[angka] = 1
            # print("test", temp[angka])
        else:
            temp[angka] = temp[angka] + 1
            # print("test 2", temp[angka])

    for total in temp:
        # print(total)
        hasil = hasil + temp[total] // 2
    return hasil

n = 9
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
result = sockMerchant(n, ar)
print("hasil", result)