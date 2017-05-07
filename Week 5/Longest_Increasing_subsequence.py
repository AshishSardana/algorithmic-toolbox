def longest_increasing_subsequense(seq):
    M = [1]*len(seq)
    for i in range(1,len(seq)):
        for j in range(i):
            if seq[i]>seq[j]:
                M[i]=max(M[i],M[j]+1)
    return max(M)
print  longest_increasing_subsequense([3,4,-1,0,6,2,3,2])
