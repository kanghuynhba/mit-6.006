def count_long_subarray(A):
    '''
    Input:  A     | Python Tuple of positive integers
    Output: count | number of longest increasing subarrays of A
    '''
    count=0
    maxLen=1
    curLen=1
    ##############
    for i in range(1, len(A)):
        if A[i]>A[i-1]:
            curLen+=1
        else:
            curLen=1
            
        if curLen==maxLen:
            count+=1
        elif curLen>maxLen:
            maxLen=curLen
            count=1
    ##############
    return count
