from collections import defaultdict

def hashing(count):
    # Convert the frequency list into a hashable string
    return ','.join(map(str, count))


def count_anagram_substrings(T, S):
    '''
    Input:  T | String
            S | Tuple of strings S_i of equal length k < |T|
    Output: A | Tuple of integers a_i:
              | the anagram substring count of S_i in T
    '''
    A = []
    k = len(S[0])
    checker = defaultdict(int)
    hash_order = []

    # Preprocess each string in S to compute its frequency hash
    for s in S:
        count = [0] * 26
        for char in s:
            count[ord(char) - ord('a')] += 1
        hash_value = hashing(count)
        checker[hash_value] = 0
        hash_order.append(hash_value)
    
    # Compute the hash for the first window of T
    count = [0] * 26
    for i in range(k):
        count[ord(T[i]) - ord('a')] += 1
    hash_value = hashing(count)
    if hash_value in checker:
        checker[hash_value] += 1

    # Slide the window through the rest of T
    i = 0
    for j in range(k, len(T)):
        count[ord(T[i]) - ord('a')] -= 1
        count[ord(T[j]) - ord('a')] += 1
        i += 1

        hash_value = hashing(count)
        if hash_value in checker:
            checker[hash_value] += 1

    # Collect the results for each string in S
    for hash_value in hash_order:
        A.append(checker[hash_value])
    return tuple(A)
