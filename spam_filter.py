k = int(input())
seq = [int(a) for a in input()]
seq_len = len(seq)

if k==1:
    for ind, ele in enumerate(seq):
        if ele==1:
            print(" ".join([str(ind+1),str(1)]))
else:
    subseq_len = range(k,2*k) # check the subsequnces with length at most 2k
    ratio = -1
    f     = 0
    l     = k
    for sl in subseq_len: # sl: subsequence length
        sub_sum = sum(seq[0:sl])
        temp_ratio = sub_sum/sl
        if temp_ratio > ratio:
            ratio = temp_ratio
            f = 0
            l = sl
        for i in range(1,seq_len-sl+1):
            sub_sum = sub_sum - seq[i-1] + seq[i+sl-1] # using sliding window trick to save computation
            temp_ratio = sub_sum/sl
            if temp_ratio > ratio:
                ratio = temp_ratio
                f = i
                l = sl
    print(" ".join([str(f+1),str(l)]))