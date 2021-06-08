def angryProfessor(k, a):
    # Write your code here
    temp = {}
    hasil = 'YES'

    for data in a:
        if data <= 0:
            temp[data] = data

    # print("kapasitas", k)
    # print("tepat waktu", len(temp))
    if len(temp) >= k:
        hasil = "NO"

    return hasil



n, k = [4, 3]
a = [-1, -3, 4, 2]
result = angryProfessor(k, a)
print(result)


