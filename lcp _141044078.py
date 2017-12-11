# 2 String Karşılaştıran ve Divide and conquer çalışan bir algoritma tasarladım. (matchStr)
# Orta kısmı kontrol etmek için midMatchStr Fonksiyonu tasarladim.
# String Array  karşılaştırmak için matchStr Fonksiyonundan yararlanıcak şekilde divide and conquer bir algoritma tasarladim.
# Contains Method O(1) dusunursek ;
# midMatchStr(n)=O(n)
# matchStr(n)=θ(nlogn)=T(n/2)+O(n)
# longest_common_postfix(n)= θ(nlog^2 n) = T(n/2)+θ(nlogn)


# T(n) = O(n) if we think contains method O(1)
def midMatchStr(str1,str2):
    newStr=""
    size = len(str2)
    halfSize=(int)(size/2)

    for i in reversed(range(0,halfSize)):
        if (str(str1).__contains__(newStr)):
            if(str(str1).__contains__(str2[i])):
                newStr=str2[i]+newStr
            else:
                break
        else:
            break

    for i in range(halfSize,size):
        if (str(str1).__contains__(newStr)):
            if(str(str1).__contains__(str2[i])):
                newStr+=str2[i]
            else:
                break
        else:
            break
    return newStr


# T(n) = O(nlogn) = T(n/2)+O(n)
def matchStr(str1,str2):
    size = len(str2)
    halfSize=(int)(size/2)
    if str(str1).__contains__(str2):
        return str2
    elif size<2:
        return ""

    left = matchStr(str1,str2[:halfSize])
    right = matchStr(str1,str2[halfSize:])
    mid = midMatchStr(str1,str2)
    maxStr=""
    if(len(left)>len(right)):
        maxStr= left
    else:
        maxStr= right
    if len(maxStr)>len(mid):
        return maxStr
    else:
        return mid



# T(n) = T(n/2) + O(nlogn) = O(nlog^2)
def longest_common_postfix(array):
    size=len(array)
    halfSize=(int)(size/2)
    if size<1:
        return None
    elif size<2:
        return array[0]
    elif size==2:
        return matchStr(array[0],array[1])
    else:
        subTextLeft=longest_common_postfix(array[:halfSize])
        subTextRight=longest_common_postfix(array[halfSize:])
        subTextMid=matchStr(array[halfSize],array[halfSize+1])

        st = matchStr(subTextLeft,subTextRight)
        return matchStr(subTextMid,st)

"""
inpStrings = ["absorptivity", "circularity", "electricity", "importunity", "humanity"]
lcp = longest_common_postfix(inpStrings)
print(lcp)
#Output: ity
"""