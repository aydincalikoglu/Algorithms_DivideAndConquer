# HoarePartition , LomutoPartition gore daha az swap yapiyor.
# iki method esit comparison yapiyor.
# sirali listelerde hoare partition daha iyi calisiyor.
# bu durumda Hoare partition daha iyi

def HoarePartition(arr, start, end):
    i = start
    j = end - 1
    while True:
        while arr[i] <= arr[end] and i < j:
            i += 1

        while arr[j] >= arr[end] and i < j:
            j -= 1

        if i == j:
            if arr[i] <= arr[end]:
                i += 1

            arr[i], arr[end] = arr[end], arr[i]
            return i
        else:
            arr[i], arr[j] = arr[j], arr[i]


def LomutoPartition(arr, start, end):
    x = arr[end]
    i = start - 1
    for j in range(start, end):
        if arr[j] <= x:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1


def quickSortHoareHelper(arr, start, end):
    if start < end:
        pivot = HoarePartition(arr, start, end)
        quickSortHoareHelper(arr, start, pivot - 1)
        quickSortHoareHelper(arr, pivot + 1, end)
    return arr

def quickSortLomutoHelper(arr, start, end):
    if start < end:
        pivot = LomutoPartition(arr, start, end)
        quickSortLomutoHelper(arr, start, pivot - 1)
        quickSortLomutoHelper(arr, pivot + 1, end)
    return arr

def quickSortHoare(arr):
    return quickSortHoareHelper(arr,0,len(arr)-1)
def quickSortLomuto(arr):
    return quickSortLomutoHelper(arr,0,len(arr)-1)


"""
arr = [15,4,68,24,75,16,42]
qsh = quickSortHoare(arr)
print(qsh)
#Output: [4, 15, 16, 24, 42, 68, 75]
qsl = quickSortLomuto(arr)
print(qsl)
#Output: [4, 15, 16, 24, 42, 68, 75]
"""