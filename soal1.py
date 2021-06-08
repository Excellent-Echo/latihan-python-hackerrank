n = 9
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]


def sockMerchant(n, ar):
    count = 0
    dict = {}

    for i in ar:
        dict[i] = dict.get(i, 0) + 1

    for i in dict.keys():
        count += dict[i] // 2

    return count


print(sockMerchant(n, ar))
