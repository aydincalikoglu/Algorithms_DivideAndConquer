# T(n) = log(k) = log(index)
# her defasinda kucuk olandan index yarisi kadar basindan kesiyor
# index yarisi kadar azaldigindan logk zamanda hesaplaniyor.
def find_kth_book_2(m, n, index):
    print(m,n,index)
    mSize = len(m)
    nSize = len(n)

    if index == 0 or index > (mSize) + (nSize):
        return None
    if index == 1:
        return m[0] if (m[0] < n[0]) else n[0]
    
    halfIndex = index // 2

    if halfIndex - 1 >= mSize:
        if m[mSize - 1] < n[halfIndex - 1]:
            return n[(index - (mSize) - 1)]
        else:
            return find_kth_book_2(m, n[halfIndex:], index - halfIndex)

    if halfIndex - 1 >= nSize:
        if n[nSize - 1] < m[halfIndex - 1]:
            return m[(index - (nSize) - 1)]
        else:
            return find_kth_book_2(m[halfIndex:], n, index - halfIndex)

    else:
        if m[halfIndex - 1] < n[halfIndex - 1]:
            return find_kth_book_2(m[halfIndex:], n, index - halfIndex)
        else:
            return find_kth_book_2(m, n[halfIndex:], index - halfIndex)

"""
m = ["algotihm", "oop", "systemsprogramming", "zebra"]
n = ["computergraphics", "cprogramming", "programminglanguages", "zort"]
#
# m = [0, 2, 9, 15]
# n = [1, 3, 4, 5]
book = find_kth_book_2(m, n, 4)
print(book)
# Output: oop
book = find_kth_book_2(m, n, 6)
print(book)
"""