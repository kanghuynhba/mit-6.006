from counting_sort import counting_sort

def radix_sort(A):
    n=len(A)
    u=1+max([x.key for x in A]) # O(n) find maximum key
    c=1+(u.bit_length()//n.bit_length())

    class Obj: pass
    D=[Obj() for a in A]

    for i in range(n): # O(nc) make digit tuples
        D[i].digits=[]
        D[i].item=A[i]
        high=A[i].key
        for j in range(c): # O(c) make digit tuple
            high, low=divmod(high, c)
            D[i].digits.append(low)
    
    for i in range(c):  # O(nc) sort each digit
        for j in range(n):  # O(n) assign key i to tuples
            D[j].key=D[j].digits[i] 
        counting_sort(D)    # O(n) sort on digit i    
    for i in range(n):  # O(n) output to A
        A[i]=D[i].item

