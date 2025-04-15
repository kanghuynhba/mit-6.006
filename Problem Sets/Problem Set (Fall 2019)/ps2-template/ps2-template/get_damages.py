def get_damages(H):
    '''
    Input:  H | list of bricks per house from west to east
    Output: D | list of damage per house from west to east
    '''
    D = [1 for _ in H]
    A=[]
    for i in range(len(H)):
        A.append((H[i], i))
        
    def mergeSort(left, right): 
        if left<right:
            mid=(left+right)//2
            mergeSort(left, mid)
            mergeSort(mid+1, right)
            merge(left, mid, right)

    def merge(left, mid, right):
        i=j=0
        count=0
        k=left
        L=A[left:mid+1]
        R=A[mid+1:right+1]
        while i<len(L) and j<len(R):
            if L[i][0]>R[j][0]:
                D[L[i][1]]+=1
                A[k]=R[j]
                j+=1
                count+=1
            else:
                A[k]=L[i]
                if i+1<len(L):
                    D[L[i+1][1]]+=count
                i+=1
            k+=1
        while i<len(L):
            A[k]=L[i]    
            if i+1<len(L):
                D[L[i+1][1]]+=count
            i+=1
            k+=1
        while j<len(R):
            A[k]=R[j]
            j+=1
            k+=1

    mergeSort(0, len(A)-1)

    return D

    