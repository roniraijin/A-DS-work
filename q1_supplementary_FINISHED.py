from random import randint

def compute_winner(history_A, history_B):
    n1 = 0
    p1 = 0
    n2 = 0
    p2 = 0
    for x in history_A:
        if x == 'H':
            n1 +=1
            if n1 > p1:
                p1 = n1
        elif x == 'T':
            p1 = n1
            n1 = 0
    for x in history_B:
        if x == 'H':
            n2 +=1
            if n2 > p2:
                p2 = n2
        elif x == 'T':
            p2 = n2
            n2 = 0
    
    if p2 > p1:
        print("B")
        return 'B'
        
    elif p1 > p2:
        print('A')
        return 'A'
       
    elif p1 == p2:
        print('D')
        return 'D'
    
    
x = 0
def encode(history):
    counter = 0
    compressed_history = ''
    for i in range(0,len(history)):
        counter = counter + 1
        if i == 0:
            compressed_history += (history[i]+str(counter))
        elif history[i] == history[i-1]:
            
            compressed_history = compressed_history[:-2]
            compressed_history += (history[i-1] + str(counter))
            
        else:
            counter = 1
            compressed_history += (history[i]+str(counter))
    return compressed_history
    
    
    
    

def decode(compressed_history):
    history = ''
    for i in range(0,len(compressed_history),2):
        if compressed_history[i] == 'H':
            for x in range(0,int(compressed_history[i+1])):
                history = history + 'H'
        if compressed_history[i] == 'T':
            for x in range(0,int(compressed_history[i+1])):
                history = history + 'T'
    return history


def compute_winner_compressed(compressed_history_A, compressed_history_B):
    h_counterA = 0
    h_counterB = 0

    for i in range(1, len(compressed_history_A), 2):
        if compressed_history_A[i-1] == 'H':
            if int(compressed_history_A[i]) > h_counterA:
                h_counterA = int(compressed_history_A[i])

    for i in range(1, len(compressed_history_B), 2):
        if compressed_history_B[i-1] == 'H':
            if int(compressed_history_B[i]) > h_counterB:
                h_counterB = int(compressed_history_B[i])
    if h_counterA > h_counterB:
        return 'A'
    elif h_counterA < h_counterB:
        return 'B'
    elif h_counterA == h_counterB:
        return 'D'
    
    
    
    
    
   

# simple tests
assert(compute_winner('HHH', 'TTT') == 'A')
assert(compute_winner('THTH', 'THHT') == 'B')
assert(compute_winner('HH', 'HH') == 'D')

assert(encode('HTTH') == 'H1T2H1')
assert(encode('TTTT') == 'T4')

assert(decode('T2') == 'TT')
assert(decode('T1H2T1') == 'THHT')

assert(compute_winner_compressed('H3', 'T3') == 'A')
assert(compute_winner_compressed('T1H1T1H1', 'T1H2T1') == 'B')
assert(compute_winner_compressed('T2', 'T2') == 'D')