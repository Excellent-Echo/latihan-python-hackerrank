k = 2
a = [0, -1, 2, 1]


def angryProfessor(k, a):
    on_time = 0

    for i in range(len(a)):
        if a[i] <= 0:
            on_time += 1

    if on_time >= k:
        return "NO"
    else:
        return "YES"


print(angryProfessor(k, a))
