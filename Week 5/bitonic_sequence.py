def bitonic_sequence(seq):
    M1 = [1]*len(seq)
    M2 = [1]*len(seq)

    for i in range(1,len(seq)):
        for j in range(i):
            if seq[i]>seq[j]:
                M1[i]=max(M1[i],M1[j]+1)

    for i in range(len(seq)-2,-1,-1):
        for j in range(i):
            if seq[i]>seq[j]:
                M2[i]=max(M2[i],M2[j]+1)

    max_val = 0
    for i in range(len(seq)):
        if M1[i]+M2[i]-1>max_val:
            max_val=M1[i]+M2[i]-1
    return max_val

print  longest_increasing_subsequense([1,4,3,7,2,1,8,11,13,0])
