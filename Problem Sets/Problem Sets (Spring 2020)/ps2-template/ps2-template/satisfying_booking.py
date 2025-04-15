def satisfying_booking(R):
    '''
    Input:  R | Tuple of |R| talk request tuples (s, t)
    Output: B | Tuple of room booking triples (k, s, t)
              | that is the booking schedule that satisfies R
    '''
    B = []

    start=[]
    end=[]
    
    for i in range(len(R)):
        start.append(R[i][0])
        end.append(R[i][1])

    mergeSort(start, 0, len(start)-1)
    mergeSort(end, 0, len(end)-1)

    i=0
    j=0
    k=0
    while i<len(start):
        while i+1<len(start) and start[i+1]<end[j]:
            k+=1
            appendIntoB(B, k, start[i], start[i+1])
            i+=1
        k+=1
        appendIntoB(B, k, start[i], end[j])
        i+=1
        if i<len(start):
            while j+1<len(end) and end[j+1]<start[i]:
                k-=1
                appendIntoB(B, k, end[j], end[j+1])
                j+=1
            k-=1
            appendIntoB(B, k, end[j], start[i])
            j+=1
    while j+1<len(end):
        k-=1
        appendIntoB(B, k, end[j], end[j+1])
        j+=1
    return tuple(B)

def appendIntoB(B, k, start, end):
    if k>0 and start!=end:
        lastId=len(B)-1
        if lastId>=0 and B[lastId][0]==k and B[lastId][2]==start:
            B[lastId]=(k,B[lastId][1], end)
        else:
            B.append((k, start, end))

def mergeSort(A, left, right):
    if left<right:
        mid=(left+right)//2
        mergeSort(A, left, mid)
        mergeSort(A, mid+1, right)
        merge(A, left, mid, right)

def merge(A, left, mid, right):
    i=0
    j=0
    k=left
    L=A[left:mid+1]
    R=A[mid+1:right+1]
    while i<len(L) and j<len(R):
        if L[i]<R[j]:
            A[k]=L[i]
            i+=1
        else:
            A[k]=R[j]
            j+=1
        k+=1
    
    while i<len(L):
        A[k]=L[i]
        i+=1
        k+=1

    while j<len(R):
        A[k]=R[j]
        j+=1
        k+=1
