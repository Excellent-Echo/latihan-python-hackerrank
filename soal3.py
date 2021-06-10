import math

array = [1,2,3,5,4,3,1,4,5]

def migrator(arr):
    birds = [0]*len(arr)
    for i in arr :
        birds[i] += 1
    print(birds)

    mak = max(birds)
    return birds.index(mak)

print(migrator(array))