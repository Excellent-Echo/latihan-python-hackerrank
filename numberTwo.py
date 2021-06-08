def angryProfessor(k, a):
    # Write your code here
    temp = 0

    for data in a:
        if data <= 0:
            temp += 1

    # print("kapasitas", k)
    # print("tepat waktu", len(temp))
    if temp >= k:
        hasil = "NO"
    else:
        hasil = "YES"

    return hasil



n, k = [4, 3]
a = [-1, -3, 4, 2]
result = angryProfessor(k, a)
print(result)


