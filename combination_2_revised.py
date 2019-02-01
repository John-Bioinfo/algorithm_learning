

a="ATCG"
def getComb(strA):
    outL = []
    charN = len(strA)
    x = strA[0]

    i = 0
    j = 0
    
    while j <= charN:
        x += strA[i]
        outL.append(x)
        i += 1           
        if i == charN :
            j += 1
            if j==charN:
                break
            x = strA[j] + x
            i = 0
        x = x[:1]
    return outL

res = getComb(a)
print(res)

res1 = getComb("3456789")
print(res1)

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

