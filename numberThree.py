

def migratoryBirds(n, arr):
    # Write your code here
    bird = [0, 0, 0, 0, 0, 0]

    for number in arr:
        bird[number] += 1

    maxs = max(bird)
    for n in range(0, len(bird)):
        if bird[n] >= maxs:
            maxs = bird[n]

    index = bird.index(maxs)
    # print('The index of e:', index)

    return index


n = 6
arr = [1, 4, 4, 4, 5, 3]
result = migratoryBirds(n, arr)
print(result)
