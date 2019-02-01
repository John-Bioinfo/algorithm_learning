
import copy

a="ATCG"
def getComb(strA):
    outL = []
    charN = len(strA)
    tmp_s = [strA[0]] * 2

    i = 0
    j = 0
    while j < charN:
        tmp_s[1] = strA[i]
        i += 1
           
        if i == charN :             
            tmp_s[0] = strA[j]
            j += 1
            i = 0
            
        OL = copy.copy(tmp_s)
        outL.append(OL)
    return outL

res = getComb(a)
print(res)

res1 = getComb("3456789")
print(len(res1))

#0 0
#0 1
#0 2
#0 3

#1 0
#1 1
#1 2
#1 3

#2 0
#2 1
#2 2
#2 3

#3 0
#3 1
#3 2
#3 3

## ref  https://stackoverflow.com/questions/53907891/number-of-k-combinations-for-all-n

