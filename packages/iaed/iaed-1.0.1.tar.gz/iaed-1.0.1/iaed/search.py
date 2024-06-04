''' Algoritmos de pesquisa '''
def binary_search(array, value, l=0, r=None) : # array must be sorted
    ''' Pesquisa binária em vetor ordenado '''
    if r is None:
        r = len(array) # return index or None
    print(l, r)
    if r <= l :
        return None
    mid = l + (r - l) // 2
    if array[mid] == value :
        return mid
    if array[mid] > value :
        return binary_search(array, value, l, mid-1)
    return binary_search(array, value, mid+1, r)

def sorted_search(array, value) : # array must be sorted
    ''' Pesquisa linear ordenada '''
    for pos, val in enumerate(array) :
        if val == value :
            return pos
        if val > value :
            return None # give up
    return None

def search(array, value) :
    ''' Pesquisa linear '''
    for pos, val in enumerate(array) :
        if val == value :
            return pos
    return None
