def repeatedString(s, n):
    # Write your code here
    a = 0
    for word in s:
        if word == "a":
            a += 1

    b = n // len(s)

    c = 0
    last = s[:n % len(s)]
    for huruf in last:
        print(huruf)
        if huruf == "a":
            c += 1

    hasil = a * b + c
    return hasil


s = "aba"
n = 10
result = repeatedString(s, n)
print(result)