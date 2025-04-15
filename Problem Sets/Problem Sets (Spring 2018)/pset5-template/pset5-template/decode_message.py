def convert_to_char(k):
    mod = k % 27
    if mod == 26:
        return ' '
    return chr(97 + mod)

def decode_message(sequence):
    '''
    Decode hidden message based on permutation of triples
    Input:  list of non-negative integers
    Output: string corresponding to hidden message
    '''
