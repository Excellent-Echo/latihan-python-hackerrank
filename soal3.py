import math

arr = [1, 2, 3, 5, 4, 4, 3, 2, 1, 3, 4]


def migratorBirds(arr):
    bird_count = [0]*len(arr)
    for i in arr:
        bird_count[i] += 1
    print(bird_count)

    maks = max(bird_count)
    return bird_count.index(maks)


print(migratorBirds(arr))
