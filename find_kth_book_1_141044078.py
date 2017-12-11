# index degeri 2 array index degerlerinin yarisindan buyuk ise
# arraylarin ortancalarina bakarak kucuk olan arrayi basindan ortasindan kesiyorum
# kucuk ise
# sonunu ortasından keserek her loop da 1 arrayi %50 azaltiyorum.
# böylece T(n) =  log ( n ) + log (m) calisma suresini elde ediyorum.
# array size'larına gore azalttigindan logm + logn suruyor.
def find_kth_book_1(m, n, index):
    mSize = len(m)
    nSize = len(n)
    halfN = (int)(nSize / 2)
    halfM = (int)(mSize / 2)

    if mSize+nSize<index:
        return None

    if not m:
        return n[index-1]
    if not n:
        return m[index-1]

    if halfM + halfN < index-1:
        if m[halfM] > n[halfN]:
            return find_kth_book_1(m, n[halfN + 1:], index - halfN -1)
        else:
            return find_kth_book_1(m[halfM + 1:], n, index - halfM -1)

    else:
        if m[halfM] > n[halfN]:
            return find_kth_book_1(m[:halfM], n, index)
        else:
            return find_kth_book_1(m, n[:halfN], index)

""""
m = ["algotihm", "programminglanguages", "systemsprogramming", "zebra"]
n = ["computergraphics", "cprogramming", "oop"]
#
#
# m = [0,2,6,7]
# n = [1,3,4,5]
book = find_kth_book_1(m, n, 4)
print(book)
# Output: oop
book = find_kth_book_1(m, n, 6)
print(book)
"""