# CrossMin : T(n)= O(n)
def crossMin(arr):
    start=0
    size=len(arr)
    halfSize=(int)(len(arr)/2)
    
    newArray=[]
    sum = 0;
    leftSum = float('inf');
    for i in reversed(range(0,halfSize)):
        sum = sum + arr[i];
        if (sum < leftSum):
            leftSum = sum;
            newArray.insert(0,arr[i])


    sum = 0;
    rightSum = float('inf');
    for i in range(halfSize,size):
        sum = sum + arr[i];
        if (sum < rightSum):
            rightSum = sum;
            newArray.append(arr[i])

    return newArray


def min_subarray_finder(array):
    size=len(array)
    halfSize=(int)(size/2)
    sumArray= sum(array)


    subMinArray=array
    if size<2:
        return array
    else:
        subArray0=min_subarray_finder(array[:halfSize])
        subArray1=min_subarray_finder(array[halfSize:])
        subArray2=crossMin(array)


        if sum(subArray0)<sum(subArray1):
            subMinArray=subArray0
        else :
            subMinArray=subArray1

        if  sum(subMinArray)>sum(subArray2):
            subMinArray=subArray2

    if sum(subMinArray)<sumArray:
        return subMinArray
    return array


"""
inpArr =   [1, -4, -7, 999, -13, -9, 23, -1]
msa = min_subarray_finder(inpArr)
print(msa)
print(sum(msa))
"""