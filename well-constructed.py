# well-structured
# 1. start with consonant
# The 21 consonant letters in the English alphabet are B, C, D, F, G, H, J, K, L, M, N, P, Q, R, S, T, V, W, X, Z, and usually Y.
# 2. does not contain two consecutive vowels (a, e, i, o, u)
# 3. does not contain two consecutive consonants

def Calc( size, d ):
    total = Factorial( size )
    for k, v in d.items():
        if v != 1:
            total /= Factorial( v )
    
    return total

def Factorial( size ):
    total = 1
    for i in range( 1, size + 1 ):
        total *= i

    return total

def InsertDict( d, key ):
    if key in d.keys():
        d[key] += 1
    else:
        d[key] = 1

def Solution( S ):
    if len( S ) == 1:                   return 1

    vowels = ['A', 'E', 'I', 'O', 'U']
    LConsonart = 0;                     LVowels = 0
    consonartExist = dict();            vowelsExist = dict()

    for c in S:
        if c in vowels:
            LVowels += 1
            InsertDict( vowelsExist, c )
        else: 
            LConsonart += 1
            InsertDict( consonartExist, c )
    
    if LConsonart == LVowels or LConsonart == LVowels + 1:
        return Calc( LConsonart, consonartExist ) * Calc( LVowels, vowelsExist )
        
    else:
        return 0

# -- list all possibilities
import itertools  
from itertools import permutations,combinations,product

def unique(iterable):
    seen = set()
    for x in iterable:
        if x in seen:
            continue
        seen.add(x)
        yield x
        
def Solution2(S):
    Vsamples = ["A","E","I","O","U"]    
    Vs = []; Cs = []
    for c in S:
        if c in Vsamples:
            Vs.append(c)
        else:
            Cs.append(c)
            
    LenVs = len(Vs); LenCs = len(Cs)
    if LenVs - LenCs > 0 or LenCs -LenVs >1: 
        return 0
    
    VPermutations =[]
    for a in unique(permutations(Vs)):
        VPermutations.append(a)
    Vlen = len(VPermutations) 
    
    CPermutations =[]
    for a in unique(permutations(Cs)):
        CPermutations.append(a)
    Clen = len(CPermutations) 
    
    count = Vlen * Clen
    # print(Vs,Cs,Vlen,Clen)
    return count

# -- test
def test( words ):
    size = len( words )
    correct = 0

    for word in words:
        res = Solution( word )
        c = Solution2( word )
        
        if c == res:
            correct += 1
        else:
            print( "String: {0}, Should be: {1}, but {2}".format( word, c, res) )

    print( "total: {0}, correct: {1}, ratio: {2}".format( size, correct, correct/size ) )

words = ["TTBBAAAA", "TTTBAAAA", "BAR", "AABB", "AABCY", "BABAC", "BABACA", "BABABA", "TTBBCCAAAAAA", 
        "TTTBBBCCCAAAAAAAAA", "TTTBBBCCCAAAAAAAOO"
    ]

test( words )

