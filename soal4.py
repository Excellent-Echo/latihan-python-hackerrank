s = 'aba'  # len = 3
n = 10

# abaabaabaa


def repeatedString(s, n):
    s_awal = s.count('a') * (n // len(s))  # aaaaaa
    s_sisa = s[:(n % len(s))].count('a')  # a
    # print(s_awal)
    # print(s_sisa)
    return s_awal + s_sisa


print(repeatedString(s, n))
