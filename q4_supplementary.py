import time
from array import array

def all_orderings(k):
    """
    Returns all Boldon House orderings of size k.
    """
    start = time.time()
    results = []
    current = array('i', [-1] * k)
    used = [False] * k
    
    def can_extend(pos, num): 
        if pos < 2:
            return True
        diff1 = (num - current[pos-1]) % k
        diff2 = (current[pos-1] - current[pos-2]) % k
        return diff1 >= diff2

    def backtrack(pos):
        if pos == k:
            sequence = list(current)
            print(sequence)  # Print each sequence as we find it
            results.append(sequence)
            return
            
        for num in range(k):
            if not used[num]:
                if not can_extend(pos, num):
                    continue
                    
                used[num] = True
                current[pos] = num
                backtrack(pos + 1)
                used[num] = False

    for first in range(k):
        used[first] = True
        current[0] = first
        backtrack(1)
        used[first] = False
        
        if time.time() - start > 590:  # 9.8 minutes
            print(f"\nTime limit approaching - returning partial results")
            break
    
    print(f"\nFound {len(results)} orderings in {time.time() - start:.2f} seconds")
    return results

def ordering(k):
    """
    Returns a Boldon House ordering of size k.
    """
    permutations = []
    counter = 0
    start = 0
    def factorial(k):
        total = 1
        for x in range(2, k+1):
            total *= x
        return total
   
    def make_list(k):
        return [i for i in range(k)]
    
    def is_increasing(permutation): 
        differences = []
        for i in range(1, len(permutation)):
            diff = (permutation[i] - permutation[i-1]) % k
            differences.append(diff)

        for i in range(1, len(differences)):
            if differences[i] < differences[i - 1]:
                return 'failure'
        return 'success'

    
    
    
    def permutation(list, perm):
        nonlocal counter
        if len(list) == 0: 
            if is_increasing(perm) == 'success':
                permutations.append(perm)
                counter += 1
            return
        for i in range(len(list)):
            index = list[i]
            recursive_list = list[:i] + list[i+1:]
            permutation(recursive_list, [index] + perm)
            



    list = make_list(k)
    permutation(list, [])
    print(permutations[0])
    return(permutations[0])

ordering(3)

# simple test for all_orderings(k) only
# you do not have to return the Boldon House orderings in exactly the same order as they appear in this test case
assert(set(tuple(o) for o in all_orderings(3)) == 
       set(tuple(o) for o in [[0, 2, 1], [0, 1, 2], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]]))





    