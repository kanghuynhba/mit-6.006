def find_peak_2D(A, r = None, w = None):
    ''' 
    Find a peak in a two dimensional array.
    Input: 2D integer array A, subarray indices r, witness w
    '''
    if r is None:
        r = (0, 0, len(A[0]) - 1, len(A) - 1)
    px, py, qx, qy = r  # A[py][px] upper left, A[qy][qx] lower right
    if w is None:
        w = (0, 0)
    wx, wy = w          # A[wy][wx] witness
    ##################
    # YOUR CODE HERE #
    ##################
    return (0, 0)
