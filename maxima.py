


def find_maxima(arr):
    index = 0
    for i in range(1, len(arr)):
        if arr[i] > arr[index]:
            index = i
    print index

find_maxima([4,2,3])
find_maxima([0,2,3])


"pIES"
