import copy

a="ATCG"
def getComb(strA,  n):
    outL = []
    sn = len(strA)
    tmp_ind = [0] * n
    
    buildL = [""] * n

    x = 0
    while x < sn ** n:
        
        for i in range(n):
            if tmp_ind[i] == sn:
                tmp_ind[i] = 0
                if i + 1 < n:
                    tmp_ind[i+1]+=1
                
            buildL[i] = strA[tmp_ind[i]]
        tmpL = copy.copy(buildL)
        outL.append(tmpL)
        
        tmp_ind[0] +=1
        x += 1
        
    return outL

res = getComb(a, 4)
print (len(res))

for i in res:
    print(''.join(i))
