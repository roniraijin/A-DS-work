import random as ran
def SelectPivotPair(L):
    """Return a pair (P0,P1) of pivot elements

    Select 5 distinct random elements from L, sort them,
    and let P0 be the second smallest and P1 the
    second largest of those 5 elements.
    """
    distinct = []
    if len(L) >= 5:
        if len(L) <= 10:
            L.sort()
            P0 = L[1]
            P1 = L[len(L)-2]
            return(P0,P1)
        else:
            for i in range(0,5):
                x = ran.choice(L)
                distinct.append(x)
    else:
        L.sort()
        return L
    distinct.sort()
    P0 = distinct[1]
    P1 = distinct[3]
    return(P0,P1)

def ThreePartition(L,P0,P1):
    """Return a triple (L0,L1,L2) of sublists of L

    L0 consists of all elements of L smaller or equal P0,
    L1 of all elements of L larger than P0 but smaller or
    equal P1, and L2 of all elements of L larger than P1
    """
    L0 = []
    L1 = []
    L2 = []
    for i in L:
        if i <= P0:
            L0.append(i)
        elif i > P0 and i <= P1:
            L1.append(i)
        elif i > P1:
            L2.append(i)
    return L0,L1,L2



def ThreeWayQuickSort(L):
    """Return a sorted version of L

    Use SelectPivotPair, ThreePartition and recursive
    calls to sort L.
    """
    if len(L) <= 4:
        return L
    P0, P1 = SelectPivotPair(L)
    L0, L1, L2 = ThreePartition(L,P0,P1)
    Paritions = [L0,L1,L2]
    if len(L) <= 10:
        L.sort()
        return(L)
    
    else:
        for i in Paritions:
            if len(i) <= 10:
                i.sort()
            else:
                i = ThreePartition(i)
        

        return L0 + L1 + L2

    
   


            


            



# simple tests

#assert SelectPivotPair([5,4,3,2,1]) == (2,4)

#assert ThreePartition([3,2,1],1,2) == ([1],[2],[3])

print(ThreeWayQuickSort([5, 3, 5, 3, 5, 6]))

