

def migratoryBirds(n, arr):
    # Write your code here
    count = [0] * 6

    for bird in arr:
        count[bird] += 1

    maxs = max(count)
    for n in range(0, len(count)):
        print("index {}: {}".format(n, count[n]))
        if count[n] >= maxs:
            maxs = count[n]
    print(maxs)

    return maxs


n = 6
arr = [1, 4, 4, 4, 5, 3]
result = migratoryBirds(n, arr)
print(result)
