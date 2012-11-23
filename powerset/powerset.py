def powerset(U):
    """Generating the entire powerset of U. Each element (a subset of U)
    is yielded as a list. Iterate with a loop to get all the elements.

    -- Author: Mads Dyrholm, mistermads@gmail.com --
       November 2012.
       
    Example
    =======

    # print out an entire powerset...
    for E in powerset([1,2,3,4,5]): print E
    """
    for j in range(0,len(U)+1):
        for E in powersetj(U,j):
            yield E
    
def powersetj(U,j):
    """Generating all possible cardinality-j subsets of U. Each
    element (a subset of U) is yielded as a list. Iterate with a loop
    to get all the elements. Throws an IndexError if j is larger than len(U).

    -- Author: Mads Dyrholm, mistermads@gmail.com --
       November 2012.

    Example
    =======

    # print all cardinality-3 subsets...
    for E in powersetj([1,2,3,4,5],3): print E
    """
    if j>len(U): raise IndexError("Desired subset cardinality is larger than the input set.")
    E = list(range(0,j))
    for item in powersetjsub(U,j,E): yield item

# --- Auxiliary subroutines ---

def powersetjsub(U,s,E):
    """Used by powersetj()"""
    if s>0:
        for i in range(1,len(U)-s+2):
            E[s-1] = U[i-1]
            for item in powersetjsub(U[i:],s-1,E): yield item
    else: yield E

# --- Test area ---

if __name__ == '__main__':
    for E in powerset([1,2,3,4,5]): print E
else:
    pass
