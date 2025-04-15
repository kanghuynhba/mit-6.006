from collections import defaultdict

def hashing(count):
    # Convert the frequency list into a hashable string representation
    return ','.join(map(str, count))

def convert_to_vector(s):
    # Convert the string representation back to a frequency list
    return list(map(int, s.split(',')))

def decode(count):
    # Decode the frequency list into the corresponding string
    result = []
    for i, freq in enumerate(count):
        result.append(chr(i + ord('a')) * freq)
    return ''.join(result)

def get_min(a, b):
    # Compare two frequency strings lexicographically
    count_a = convert_to_vector(a)
    count_b = convert_to_vector(b)
    for x, y in zip(count_a, count_b):
        if x > y:
            return a
        elif x < y:
            return b
    return a

def most_likely_hand(D, k):
    '''
    Input:  D | string of length n representing the deck
            k | integer representing hand size
    Output: H | string of length k representing the most likely hand
    '''
    ##################
    # YOUR CODE HERE #
    freq = defaultdict(int)  # Frequency map for substrings
    count = [0] * 26         # Frequency table for the current window

    # Initialize the first window
    for i in range(k):
        count[ord(D[i]) - ord('a')] += 1
    
    ans = hashing(count)
    max_count = 1
    freq[ans] = 1
    i = 0

    # Slide the window through the string
    for j in range(k, len(D)):
        count[ord(D[i]) - ord('a')] -= 1
        count[ord(D[j]) - ord('a')] += 1
        i += 1

        t = hashing(count)
        if t not in freq:
            freq[t] = 0
        freq[t] += 1

        if freq[t] > max_count:
            ans = t
            max_count = freq[t]
        elif freq[t] == max_count:
            ans = get_min(ans, t)
    
    # Decode the result back into a string and print
    arr = convert_to_vector(ans)
    return decode(arr) 


